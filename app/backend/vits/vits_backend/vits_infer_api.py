import numpy as np
import torch
import commons
import utils
from models import SynthesizerTrn
from text.symbols import symbols
from text import text_to_sequence
from scipy.io import wavfile
import time
import os
from playsound import playsound
import re

# text preprocessing using cleaners
def get_text(text, hps):
    text_norm = text_to_sequence(text, hps.data.text_cleaners)
    if hps.data.add_blank:
        text_norm = commons.intersperse(text_norm, 0)
    text_norm = torch.LongTensor(text_norm)
    return text_norm


def save_wav(wav, path, rate):
    wav *= 32767 / max(0.01, np.max(np.abs(wav))) * 0.6
    wavfile.write(path, rate, wav.astype(np.int16))


class VitsInfer:
    def __init__(self, ):
        # use GPU or CPU to infer
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        file_path = os.path.abspath(__file__)
        self.module_dir = os.path.dirname(file_path)

        # load hyperparameters
        self.hps = utils.get_hparams_from_file(os.path.join(self.module_dir, "configs/Cyberpunk_base.json"))

        # initialize network
        self.net_g = SynthesizerTrn(
            len(symbols),
            self.hps.data.filter_length // 2 + 1,
            self.hps.train.segment_size // self.hps.data.hop_length,
            **self.hps.model)

        self.net_g.to(self.device)
        self.net_g.eval()

        # load pretrained model
        utils.load_checkpoint(os.path.join(self.module_dir, "pretrained_model.pth"), self.net_g, None)

        print("VITS initialized... Inference device:%s" % self.device)

    def generate_audio(self, item):
        # length of the audio
        length_scale = 1

        stn_tst = get_text(item, self.hps)
        with torch.no_grad():
            x_tst = stn_tst.to(self.device).unsqueeze(0)
            x_tst_lengths = torch.LongTensor([stn_tst.size(0)]).to(self.device)
            audio = \
                self.net_g.infer(x_tst, x_tst_lengths, noise_scale=.667, noise_scale_w=0.8, length_scale=length_scale)[
                    0][
                    0, 0].data.cpu().float().numpy()
            audio_path = self.module_dir + "/vits_infer_out/vits.wav"
            save_wav(audio, audio_path, self.hps.data.sampling_rate)
            playsound(audio_path)
            return audio_path

    def generate_audio_v1(self, text_item):
        text, filename = text_item
        # length of the audio
        length_scale = 1
        stn_tst = get_text(text_item, self.hps)
        with torch.no_grad():
            x_tst = stn_tst.to(self.device).unsqueeze(0)
            x_tst_lengths = torch.LongTensor([stn_tst.size(0)]).to(self.device)
            audio = \
                self.net_g.infer(x_tst, x_tst_lengths, noise_scale=.667, noise_scale_w=0.8, length_scale=length_scale)[
                    0][
                    0, 0].data.cpu().float().numpy()
            audio_path = self.module_dir + "/vits_infer_out/" + filename
            save_wav(audio, audio_path, self.hps.data.sampling_rate)
            # playsound(audio_path)
            return audio_path

    def generate_audio_v2(self, text_item):
        text, filename = text_item
        # length of the audio
        length_scale = 1
        # items = re.findall(r'[^。；！？.;!]+[。；！？.;!]', text)
        stn_tst = get_text(text, self.hps)
        with torch.no_grad():
            x_tst = stn_tst.to(self.device).unsqueeze(0)
            x_tst_lengths = torch.LongTensor([stn_tst.size(0)]).to(self.device)
            audio = \
                self.net_g.infer(x_tst, x_tst_lengths, noise_scale=.667, noise_scale_w=0.8, length_scale=length_scale)[
                    0][
                    0, 0].data.cpu().float().numpy()
            return audio


if __name__ == "__main__":
    prompt = "从前，有一个叫做阿里巴巴的年轻人，他是一个小商贩，但他的生意并不太好。"
    t0 = time.time()
    vits = VitsInfer()
    t1 = time.time()
    vits.generate_audio(prompt)
