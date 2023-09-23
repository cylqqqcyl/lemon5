from .hubconf import knn_vc
import torch

_global_knnvc = None
_global_device = None       
_global_hps = None         


def knnvc_initialize(pretrained=True, progress=True, prematched=True):
    """
    initialize knn-vc instance
    """
    global _global_device
    global _global_hps
    global _global_knnvc
    _global_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    _global_knnvc = knn_vc(pretrained, progress, prematched, device = _global_device)


def voice_conversion(src, tgt):
    
    # initialize
    if _global_knnvc == None:
        knnvc_initialize(pretrained=True, progress=True, prematched=True)
    src_wav_path = src
    ref_wav_path = tgt
    
    #voice conversion
    query_seq = _global_knnvc.get_features(src_wav_path)
    matching_set = _global_knnvc.get_matching_set([ref_wav_path])
    audio = _global_knnvc.match(query_seq, matching_set, topk=4).cpu().numpy()
    
    return audio
    
