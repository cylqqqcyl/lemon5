
import os
import pkg_resources
import torch

from .infer_tool import SVC

_global_device = None       # inference device
_global_converter = None    # SVC model
_global_singer = "alice"    # singer name


SINGERS = ["alice", "teio"]


def _initialize(singer="alice"):
    global _global_device
    global _global_converter
    global _global_singer

    _global_singer = singer
    _global_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    checkpoint_dir = pkg_resources.resource_filename(__name__, "checkpoints")
    _global_converter = SVC(os.path.join(checkpoint_dir, f"vits_{singer}.pth"), 
                         os.path.join(checkpoint_dir, "config_alice.json"),
                         device=_global_device)

def convert_singing_voice(wav_path, singer="alice"):

    global _global_converter

    if not _global_converter:
        _initialize(singer)

    if singer != _global_singer:
        _initialize(singer)

    # hardcode some parameters
    audio = _global_converter.slice_inference(
            wav_path, 
            spk=0,
            tran=0, 
            slice_db=-40,
            cluster_infer_ratio=0,
            auto_predict_f0=False,
            noice_scale=0.4,
            pad_seconds=0.5)
    
    # 44.1kHz
    return audio
