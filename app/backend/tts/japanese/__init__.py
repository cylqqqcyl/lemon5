import re
import numpy as np
import pkg_resources
import torch
from .utils import get_hparams_from_file, load_checkpoint
from .commons import intersperse
from .models import SynthesizerInfer
from .text import text_to_sequence
from .text.symbols import symbols

_global_device = None      # inference device
_global_hps = None          # hyper parameter
_global_synthesizer = None  # audio synthesizer

def _initialize():
    """Initialize syntheiszer
    """

    global _global_device
    global _global_synthesizer
    global _global_hps
    _global_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    _global_hps = get_hparams_from_file(pkg_resources.resource_filename(__name__, "config.json"))
    _global_synthesizer = SynthesizerInfer(
        len(symbols),
        _global_hps.data.filter_length // 2 + 1,
        _global_hps.train.segment_size // _global_hps.data.hop_length,
        **_global_hps.model).to(_global_device)
    _ = _global_synthesizer.eval()
    _ = load_checkpoint(pkg_resources.resource_filename(__name__, "model_tts_ja.pth"), _global_synthesizer, None)

def _get_sequence(text, merge=False):
    """Get sequence from text.
    """

    sequence_list = text_to_sequence(text)

    for i, sequence in enumerate(sequence_list):
        global _global_hps
        if _global_hps.data.add_blank:
            sequence = intersperse(sequence, 0)
        sequence = torch.LongTensor(sequence)
        sequence_list[i] = sequence     
   
    if merge:
        # merge sequence
        sequence = sequence_list[0]
        for i in range(1, len(sequence_list)):
            sequence = torch.cat((sequence, sequence_list[i]), dim=0)

        # long tensor sequence
        return sequence
    else:
        # list of long tensor sequence
        return sequence_list

def _synthesize_from_squence(sequence):
    """Synthesize audio from sequence.
    """

    with torch.no_grad():
        x = sequence.to(_global_device).unsqueeze(0)
        x_lengths = torch.LongTensor([x.size(1)]).to(_global_device)
        audio = _global_synthesizer(x, x_lengths, noise_scale=.667, noise_scale_w=0.8, length_scale=1.0)[0][0,0].data.cpu().float().numpy()

    return audio


def synthesize(text, accelerate=False):
    """Synthesize audio from text.
    """

    # initialize
    if _global_synthesizer is None:
        _initialize()

    # slow sythesis
    if not accelerate:
        sequence = _get_sequence(text, merge=True)
        audio = _synthesize_from_squence(sequence)
    # TODO: fast synthesis (WIP)
    else:
        raise NotImplementedError("Fast synthesis is not supported yet.")
        sequence_list = _get_sequence(text, merge=False)
        audio_list = []
        for sequence in sequence_list:
            audio = _synthesize_from_squence(sequence)
            audio_list.append(audio)
        audio = audio_list[0]
        for i in range(1, len(audio_list)):
            audio = np.concatenate((audio, audio_list[i]))

    return audio
