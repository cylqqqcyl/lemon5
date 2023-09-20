import json
import pkg_resources
import torch
import librosa

from .util import sampling
from .network import CleanUNet


_global_device = None
_global_denoiser = None

def _initialize():
    """Initialize denoiser.
    """

    global _global_device
    global _global_denoiser
    _global_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    with open(pkg_resources.resource_filename(__name__, "config.json")) as f:
        data = f.read()
        config = json.loads(data)
    # define network
    network_config = config["network_config"]
    _global_denoiser = CleanUNet(**network_config).to(_global_device)

    # load checkpoint
    checkpoint = torch.load(pkg_resources.resource_filename(__name__, "se_model.pkl"), map_location='cpu')
    _global_denoiser.load_state_dict(checkpoint['model_state_dict'])
    _global_denoiser.eval()

def _load_audio(audio_path):
    audio, sr = librosa.load(audio_path)
    audio = librosa.to_mono(audio)
    audio = librosa.resample(audio, orig_sr=sr, target_sr=16000)
    audio = torch.from_numpy(audio)
    audio = audio.unsqueeze(0).to(_global_device)

    return audio
    
def denoise(noisy_audio_path):
    """Denoise noisy audio.
    """

    # initialize
    if _global_denoiser is None:
        _initialize()
    noisy_audio = _load_audio(noisy_audio_path)
    clean_audio = sampling(_global_denoiser, noisy_audio)
    clean_audio = clean_audio[0].squeeze().cpu().numpy()

    return clean_audio




