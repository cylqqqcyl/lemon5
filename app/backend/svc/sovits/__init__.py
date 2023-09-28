
import os
import pkg_resources
import torch

from .infer_tool import SVC

_global_device = None   # inference device
_global_singer = None   # SVC model


def _initialize():
    global _global_device
    global _global_singer
    _global_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    checkpoint_dir = pkg_resources.resource_filename(__name__, "checkpoints")
    _global_singer = SVC(os.path.join(checkpoint_dir, "vits_alice.pth"), 
                         os.path.join(checkpoint_dir, "config_alice.json"),
                         device=_global_device)


def convert_singing_voice(wav_path, sid=0):

    global _global_singer

    if not _global_singer:
        _initialize()

    # hardcode some parameters
    audio = _global_singer.slice_inference(
            wav_path, sid, 
            tran=0, 
            slice_db=-40,
            cluster_infer_ratio=0,
            auto_predict_f0=False,
            noice_scale=0.4,
            pad_seconds=0.5)
    
    # 44.1kHz
    return audio
