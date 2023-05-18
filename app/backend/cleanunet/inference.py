import json
import torch
from scipy.io.wavfile import write as wavwrite
import librosa
from util import sampling
from network import CleanUNet
import os
import shutil
from pydub import AudioSegment


# global variables
source_path = ''
export_path = 'cache/denoise_wavefile.wav' # 上传音频经过格式转换、重采样等步骤后得到音频的导出路径
flag_upload = False  # 等待输入source path
flag_denoise = False  # 是否等待启动denoise
flag_terminate = False  # 是否结束线程
device = torch.device('cpu')  # 仅支持CPU推理


class Denoiser:
    def __init__(self, ckpt_path, config_path):
        self.ckpt_path = ckpt_path
        self.config_path = config_path
        self.save_path = 'cache/denoise_denoised.wav'
        self.download_path = 'cache/denoise_download.wav'
        self.play_path = 'cache/denoise_play.wav'

        self.load_denoiser()

    def load_denoiser(self):
        # load config
        with open(self.config_path) as f:
            data = f.read()
        config = json.loads(data)

        # define network
        network_config = config["network_config"]
        net = CleanUNet(**network_config).to(device)

        # load checkpoint
        checkpoint = torch.load(self.ckpt_path, map_location='cpu')
        net.load_state_dict(checkpoint['model_state_dict'])
        net.eval()
        self.denoiser = net

    def denoise_audio(self, noisy_audio):

        clean_audio = sampling(self.denoiser, noisy_audio)
        clean_audio = clean_audio[0].squeeze().cpu().numpy()


        wavwrite(self.save_path, 16000, clean_audio)
        shutil.copy(self.save_path, self.play_path)
        shutil.copy(self.save_path, self.download_path)


def wait_upload():
    global flag_upload
    while True:
        if flag_upload:
            break


def load_audio(audio_path):
    global source_path
    global flag_upload
    if audio_path:
        source_path = audio_path
        flag_upload = True


def wait_denoise():
    global flag_denoise
    while True:
        if flag_denoise:
            break

def denoise_audio():
    global flag_upload, flag_denoise, source_path
    if source_path:
        flag_upload = True
        flag_denoise = True

def terminate_se():
    global flag_upload, flag_terminate
    flag_terminate = True
    flag_upload = True


def revise_path(origin_path):
    origin_path = origin_path.replace('\\', '/').replace('\n', '/n').replace('\r', '/r')
    revised_path = origin_path.replace('\t', '/t').replace('\a', '/a').replace('\b', '/b')

    return revised_path

# 支持将常见音频格式转成wav
def load_wav(audio_path: str):
    global source_path, source_path
    if audio_path.endswith('wav'):
        pass
    else:
        if audio_path.endswith('mp3'):
            audio = AudioSegment.from_mp3(audio_path)

        elif audio_path.endswith('ogg'):
            audio = AudioSegment.from_ogg(audio_path)

        elif audio_path.endswith('flv'):
            audio = AudioSegment.from_flv(audio_path)
        else:
            raise ValueError('Not supported audio format!')

        audio.export(export_path, format='wav')
        source_path = export_path

    source, sr = librosa.load(source_path)
    source = librosa.to_mono(source)
    source = librosa.resample(source, orig_sr=sr, target_sr=16000)
    source = torch.from_numpy(source)
    source = source.unsqueeze(0).to(device)

    return source


def denoising(model_dir):
    model_path = os.path.join(model_dir, 'model.pkl')
    config_path = os.path.join(model_dir, 'config.json')
    print('Lemon4> Loading models...')
    denoiser = Denoiser(model_path, config_path)
    print('Lemon4> Successfully loaded CleanUNet model!')

    while True:
        global flag_upload, flag_denoise, flag_terminate, source_path
        flag_upload = flag_denoise = flag_terminate = False

        print('Lemon4> Please input some audio...')
        wait_upload()

        if flag_terminate:
            print('Lemon4> Terminating...')
            break

        source_path = revise_path(source_path)
        print(f'Lemon4> Successfully loaded audio from {source_path}')

        source = load_wav(source_path)

        wait_denoise()

        print('Lemon4> Denoising...')
        try:
            denoiser.denoise_audio(source)
            print('Lemon4> Successfully denoised audio!')
        except Exception as e:
            print(e)
    print('Lemon4> Speech enhancement is terminated!')

if __name__ == '__main__':
    # debug use
    model_dir = '../../cleanunet'
    source_path = '../../cache/sample_input/sovits_src.wav'

    # 下面不用动
    model_path = os.path.join(model_dir, 'model.pkl')
    config_path = os.path.join(model_dir, 'config.json')
    denoiser = Denoiser(model_path, config_path)

    source_path = revise_path(source_path)

    source = load_wav(source_path)
    denoiser.denoise_audio(source)
