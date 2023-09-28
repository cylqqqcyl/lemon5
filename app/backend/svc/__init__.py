from sovits import convert_singing_voice
from scipy.io.wavfile import write

src_path = "/Users/hurui05/Desktop/projects/lemon5/tests/data/wavs/svc_src_ichibanhoshi_vocal.wav"
trg_path = "/Users/hurui05/Desktop/projects/lemon5/tests/data/wavs/svc_trg_ichibanhoshi_vocal.wav"


audio = convert_singing_voice(src_path)
write(trg_path, 44100, audio)
