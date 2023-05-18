import os
import torch
import librosa
from scipy.io.wavfile import write
from pydub import AudioSegment
import utils
import shutil
from models import SynthesizerTrn
from hubert import load_hubert


# global variables
source_path = ''
export_path = 'cache/sovits_wavefile.wav'  # 上传音频经过格式转换、重采样等步骤后得到音频的导出路径
flag_upload = False  # 等待输入source path
flag_convert = False  # 是否等待启动convert
flag_terminate = False  # 是否结束线程
sid_source = None  # 实际使用时，只有sid_target会用上
sid_target = None
device = torch.device('cpu')  # 仅支持CPU推理
NOISE_SCALE = 0.667
NOISE_SCALE_W = 0.8
LENGTH_SCALE = 0.6


class Sovits():
    def __init__(self,
                 hubert_path,
                 vits_path,
                 hps,
                 device,
                 save_path='cache/sovits_converted.wav',
                 play_path='cache/sovits_play.wav',
                 download_path='cache/sovits_download.wav'):

        self.hubert_path = hubert_path
        self.vits_path = vits_path
        self.save_path = save_path
        self.play_path = play_path
        self.download_path = download_path
        self.hps = hps
        self.device = device

        self.load_models()

    def load_models(self):
        try:
            hubert = load_hubert(self.hubert_path)
            self.hubert = hubert.to(self.device)
        except:
            raise FileNotFoundError('Failed to load hubert model!')

        vits = SynthesizerTrn(
            self.hps.data.filter_length // 2 + 1,
            self.hps.train.segment_size // self.hps.data.hop_length,
            n_speakers=self.hps.data.n_speakers,
            **self.hps.model)
        _ = vits.eval()

        try:
            _ = utils.load_checkpoint(self.vits_path, vits)
            self.vits = vits.to(self.device)
        except:
            raise FileNotFoundError('Failed to load vits model!')

    def inference(self, source, sid=None, noise_scale=0.667, noise_scale_w=0.8, length_scale=0.6):
        source = source.to(device)

        with torch.inference_mode():
            # extract speech units
            unit = self.hubert.units(source)
            unit = torch.FloatTensor(unit.cpu())
            unit = unit.to(device)
            unit_lengths = torch.LongTensor([unit.size(1)]).to(device)
            # convert voice
            # single speaker
            if sid is None:
                converted = self.vits.infer(
                    unit,
                    unit_lengths,
                    noise_scale=noise_scale,
                    noise_scale_w=noise_scale_w,
                    length_scale=length_scale)[0][0, 0].data.float().cpu().numpy()
            # multi-speaker
            else:
                converted = self.vits.infer(
                    unit,
                    unit_lengths,
                    sid,
                    noise_scale=noise_scale,
                    noise_scale_w=noise_scale_w,
                    length_scale=length_scale)[0][0, 0].data.float().cpu().numpy()

        # write converted audio to cache
        write(self.save_path, 22050, converted)
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


def wait_convert():
    global flag_convert
    while True:
        if flag_convert:
            break


def convert_audio():
    global flag_upload, flag_convert, source_path
    if source_path:
        flag_upload = True
        flag_convert = True


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
    source = librosa.resample(source, orig_sr=sr, target_sr=22050)
    source = librosa.to_mono(source)
    source = torch.from_numpy(source).unsqueeze(0).unsqueeze(1)

    return source


def select_speaker(speaker_id):
    global sid_target
    sid_target = torch.LongTensor([speaker_id])


def terminate_vc():
    global flag_upload, flag_terminate
    flag_terminate = True
    flag_upload = True


def voice_conversion(model_dir):
    print('Lemon4> Begin voice conversion!')
    hubert_path = os.path.join(model_dir, 'hubert.pt')
    vits_path = os.path.join(model_dir, 'vits.pth')
    config_path = os.path.join(model_dir, 'config.json')
    print('Lemon4> Loading models...')
    hps = utils.get_hparams_from_file(config_path)
    sovits = Sovits(hubert_path, vits_path, hps, device)
    print('Lemon4> Successfully loaded models!')

    while True:
        global flag_upload, flag_convert, flag_terminate, source_path, sid_source, sid_target
        flag_upload = flag_convert = flag_terminate = False

        print('Lemon4> Please input some audio...')
        wait_upload()

        if flag_terminate:
            print('Lemon4> Terminating...')
            break

        source_path = revise_path(source_path)
        print(f'Lemon4> Successfully loaded audio from {source_path}')

        source = load_wav(source_path)

        wait_convert()

        print('Lemon4> Converting (hubert mode)...')
        try:
            sovits.inference(source, sid_target)
            print('Lemon4> Successfully converted the source audio!')
        except Exception as e:
            print(e)

    print('Lemon4> Voice conversion is terminated!')


if __name__ == "__main__":
    # debug use

    model_dir = '../../sovits-nat-1'   # 模型文件夹路径
    source_path = '../../cache/sample_input/sovits_src.wav'    # 源音频路径
    sid_target = None  # 单人模型sid_target为None

    # 下面不用动
    hubert_path = os.path.join(model_dir, 'hubert.pt')
    vits_path = os.path.join(model_dir, 'vits.pth')
    config_path = os.path.join(model_dir, 'config.json')

    hps = utils.get_hparams_from_file(config_path)
    sovits = Sovits(hubert_path, vits_path, hps, device)

    source_path = revise_path(source_path)
    source = load_wav(source_path)
    sovits.inference(source, sid_target)    # 生成音频放在../../cache中

