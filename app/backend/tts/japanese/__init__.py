import re
import numpy as np
import pkg_resources
import torch
from .utils import get_hparams_from_file, load_checkpoint
from .commons import intersperse
from .models import SynthesizerInfer
from .text import text_to_sequence, symbol_to_sequence, clean_text
from .text.symbols import symbols

_global_device = None       # inference device
_global_hps = None          # hyper parameter
_global_synthesizer = None  # audio synthesizer

def _initialize():
    """Initialize syntheiszer.
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
    _ = load_checkpoint(pkg_resources.resource_filename(__name__, "tts_ja.pth"), _global_synthesizer)


def get_sequence_from_text(text):
    """Get sequence from text.
    """

    sequence = text_to_sequence(text)

    global _global_hps
    if _global_hps.data.add_blank:
        sequence = intersperse(sequence, 0)
    sequence = torch.LongTensor(sequence)
    
    return sequence


def get_sequence_from_symbol(symbols):
    sequence = symbol_to_sequence(symbols)

    global _global_hps
    if _global_hps.data.add_blank:
        sequence = intersperse(sequence, 0)
    sequence = torch.LongTensor(sequence)

    return sequence


def synthesize_from_squence(sequence):
    """Synthesize audio from sequence.
    """

    with torch.no_grad():
        x = sequence.to(_global_device).unsqueeze(0)
        x_lengths = torch.LongTensor([x.size(1)]).to(_global_device)
        audio = _global_synthesizer(x, x_lengths, noise_scale=.667, noise_scale_w=0.8, length_scale=1.0)[0][0,0].data.cpu().float().numpy()

    return audio


def synthesize(text):
    """Synthesize audio from text.
    """

    # initialize
    if _global_synthesizer is None:
        _initialize()

    # synthesis
    sequence = get_sequence_from_text(text)
    audio = synthesize_from_squence(sequence)

    return audio
