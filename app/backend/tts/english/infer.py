
import os
import json
import math
import torch
from torch import nn
from torch.nn import functional as F
from torch.utils.data import DataLoader

import commons
import utils
from models import SynthesizerTrn
from text.symbols import symbols
from text import text_to_sequence


import torchaudio
import shutil

def get_text(text, hps):
    text_norm = text_to_sequence(text, hps.data.text_cleaners)
    if hps.data.add_blank:
        text_norm = commons.intersperse(text_norm, 0)
    text_norm = torch.LongTensor(text_norm)
    return text_norm

hps = utils.get_hparams_from_file("./logs/ljs_nosdp4/config.json")

if "use_mel_posterior_encoder" in hps.model.keys() and hps.model.use_mel_posterior_encoder == True:
    print("Using mel posterior encoder for VITS2")
    posterior_channels = 80 #vits2
    hps.data.use_mel_posterior_encoder = True
else:
    print("Using lin posterior encoder for VITS1")
    posterior_channels = hps.data.filter_length // 2 + 1  
    hps.data.use_mel_posterior_encoder = False

net_g = SynthesizerTrn(
    len(symbols),
    posterior_channels,
    hps.train.segment_size // hps.data.hop_length,
    #**hps.model).cuda()
    **hps.model)
_ = net_g.eval()

#_ = utils.load_checkpoint("./logs/ljs_base/G_0.pth", net_g, None)
_ = utils.load_checkpoint("./logs/ljs_nosdp4/G_777000.pth", net_g, None)

results_folder = "./infer_audio_v103_777k"
if os.path.exists(results_folder):
    shutil.rmtree(results_folder)
os.mkdir(results_folder)
with open("./test_text.txt", 'r') as f: 
    lines = f.readlines()
    for line in lines:
        print(line)
        id = line.split("|")[0]
        text = line.split("|")[1]
        stn_tst = get_text(text, hps)
        with torch.no_grad():
            # x_tst = stn_tst.cuda().unsqueeze(0)
            # x_tst_lengths = torch.LongTensor([stn_tst.size(0)]).cuda()
            x_tst = stn_tst.unsqueeze(0)
            x_tst_lengths = torch.LongTensor([stn_tst.size(0)])
            audio = net_g.infer(x_tst, x_tst_lengths, noise_scale=.667, noise_scale_w=0.8, length_scale=1)[0][0,0].data.cpu().float().numpy()
        #ipd.display(ipd.Audio(audio, rate=hps.data.sampling_rate, normalize=False))
        torchaudio.save(os.path.join(results_folder, "v103_777k_" + id + ".wav"), torch.FloatTensor(audio).unsqueeze(0), 22050)
