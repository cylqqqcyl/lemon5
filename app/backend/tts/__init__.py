# TODO: wrapper for zh, en and ja tts.

from .japanese import synthesize as synthesze_ja


_langs = ["zh", "en", "ja"]

def synthesize(text, lang="ja"):
    """Simple wrapper for text-to-speech.
    """
    
    if lang == "ja":
        audio = synthesze_ja(text)
    elif lang == "zh":
        raise NotImplementedError("Chinese TTS is not supported yet.")
    elif lang == "en":
        raise NotImplementedError("English TTS is not supported yet.")
    else:
        raise ValueError("Not supported language {}. Expected {}."
                         .format(lang, ", ".join(_langs)))

    return audio



    