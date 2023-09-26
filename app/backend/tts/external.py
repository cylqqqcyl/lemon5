import requests
import numpy as np
import io
from scipy.io import wavfile


URL_V1 = "https://genshinvoice.top/v1/"
URL_V2 = "https://genshinvoice.top/v2/"


def synthesize_gv_v2(text: str, speaker: str, lang="zh",
                  emo_ratio: float=0.5, sdp_ratio: float=0.2, 
                  phn_len=0.9, speed: float=1.0) -> np.ndarray:
    """Genshinvoice TTS v2.

    Args:
        text (str): Text.
        speaker (str): Speaker.
        lang (str, optional): Language.
        emo_ratio (float, optional): Emotion ratio. Defaults to 0.5.
        sdp_ratio (float, optional): Duration prediction ratio. Defaults to 0.2.
        phn_len (float, optional): Phoneme length. Defaults to 0.9.
        speed (float, optional): Speed. Defaults to 1.0.

    Returns:
        np.ndarray: Audio.
    """

    pass


