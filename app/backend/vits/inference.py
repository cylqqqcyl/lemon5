import sys

sys.path.append('../vits/vits_backend')
sys.path.append('../vits')
"""
pip install playsound==1.2.2
"""
import numpy as np
import torch
import shutil
import vits_backend.commons as commons
import vits_backend.utils as utils
from vits_backend.models import SynthesizerTrn
from vits_backend.text.symbols import symbols
from vits_backend.text import text_to_sequence
from scipy.io import wavfile
import os
import pyaudio
import wave
import time
import threading
import re
import queue

# global variables
source_text = ''
flag_text = False  # 等待输入文本
flag_generate = False  # 是否等待启动合成
flag_fast_generate = False  # 是否启动快速合成
flag_terminate = False  # 是否结束线程
device = torch.device('cpu')  # 仅支持CPU推理
NOISE_SCALE = 0.667
NOISE_SCALE_W = 0.8
LENGTH_SCALE = 1


class Vits:
    def __init__(self,
                 vits_path,
                 hps,
                 device,
                 tmp_path=os.path.abspath('cache/vits_tmp.wav'),
                 save_path=os.path.abspath('cache/vits_generated.wav'),
                 fast_path=os.path.abspath('cache/vits_fast_generated.wav'),
                 play_path=os.path.abspath('cache/vits_play.wav'),
                 download_path=os.path.abspath('cache/vits_download.wav')):
        self.tmp_path = tmp_path
        self.vits_path = vits_path
        self.save_path = save_path
        self.play_path = play_path
        self.fast_path = fast_path
        self.download_path = download_path
        self.hps = hps
        self.device = device
        self.load_models()

    def load_models(self):

        vits = SynthesizerTrn(
            len(symbols),
            self.hps.data.filter_length // 2 + 1,
            self.hps.train.segment_size // self.hps.data.hop_length,
            **self.hps.model)
        _ = vits.eval()

        try:
            _ = utils.load_checkpoint(self.vits_path, vits)
            self.vits = vits.to(self.device)
        except:
            raise FileNotFoundError('Failed to load vits model!')

    def inference(self, item, noise_scale=0.667, noise_scale_w=0.8, length_scale=1):
        stn_tst = get_text(item, self.hps)
        with torch.no_grad():
            x_tst = stn_tst.to(self.device).unsqueeze(0)
            x_tst_lengths = torch.LongTensor([stn_tst.size(0)]).to(self.device)
            audio = \
                self.vits.infer(x_tst, x_tst_lengths, noise_scale=noise_scale, noise_scale_w=noise_scale_w,
                                length_scale=length_scale)[
                    0][
                    0, 0].data.cpu().float().numpy()

            save_wav(audio, self.save_path, self.hps.data.sampling_rate)
            play_audio(self.save_path)
            shutil.copy(self.save_path, self.play_path)
            shutil.copy(self.save_path, self.download_path)
            return audio, self.save_path

    def generate_audio_thread(self, text_data):

        for item in text_data:
            tmp, _ = self.inference(item)
            # print(type(tmp))
            # time.sleep(0.1)
            self.audio_queue.put(tmp)
        # Add a None value to the queue to indicate the end of audio data
        self.audio_queue.put(None)
        self.complete = True

    def play_sound_y(self, ):
        while not self.terminate_event.is_set():
            try:
                tmp = self.audio_queue.get(timeout=1)
            except queue.Empty:
                time.sleep(0.1)
                continue

            # Check if we have reached the end of audio data
            if tmp is None:
                self.terminate_event.set()
                break
            if self.complete:
                if not type(tmp) == np.ndarray:
                    play_audio(tmp)
                    # save_wav(tmp, self.tmp_path, self.vits.hps.data.sampling_rate)
                    # merge_wav_files(self.fast_path, self.tmp_path)
            else:
                if not type(tmp) == np.ndarray:
                    play_audio(tmp)
                    # save_wav(tmp, self.tmp_path, self.vits.hps.data.sampling_rate)
                    # merge_wav_files(self.fast_path, self.tmp_path)

    def inference_fast(self, new_string):

        text_data_list = parse(new_string)

        self.audio_queue = queue.Queue()
        self.terminate_event = threading.Event()

        p1 = threading.Thread(target=self.generate_audio_thread, args=(text_data_list,))
        p2 = threading.Thread(target=self.play_sound_y, )

        self.complete = False
        p1.start()
        p2.start()
        # Wait for the termination event to be set before terminating the threads
        self.terminate_event.wait()

        # Signal the termination event to the producer and consumer threads
        # print("task done. terminating", flush = True)
        p1.join()
        p2.join()

        while not self.audio_queue.empty():
            _ = self.audio_queue.get()


def parse(my_string):
    items = re.findall(r'[^。；！？.;!]+[。；！？.;!]', my_string)  # VITS works best when generating whole sentences
    # items = re.split('[^\w]+', my_string)

    while "" in items:
        items.remove("")
    text_data_list = list(zip(*[items]))
    print()
    return text_data_list


def get_text(text, hps):
    text_norm = text_to_sequence(text, hps.data.text_cleaners)
    if hps.data.add_blank:
        text_norm = commons.intersperse(text_norm, 0)
    text_norm = torch.LongTensor(text_norm)
    return text_norm


def save_wav(wav, path, rate):
    wav *= 32767 / max(0.01, np.max(np.abs(wav))) * 0.6
    wavfile.write(path, rate, wav.astype(np.int16))

def merge_wav_files(file1, file2):
    # 重命名第一个 wav 文件为临时文件名
    temp_file = "temp.wav"
    shutil.move(file1, temp_file)

    # 打开临时文件并获取相关信息
    with wave.open(temp_file, 'rb') as wav1:
        sample_width = wav1.getsampwidth()
        channels = wav1.getnchannels()
        framerate = wav1.getframerate()
        frames1 = wav1.readframes(wav1.getnframes())

    # 打开第二个 wav 文件并获取相关信息
    with wave.open(file2, 'rb') as wav2:
        frames2 = wav2.readframes(wav2.getnframes())

    # 将两个 wav 文件的音频数据写入临时文件中
    with wave.open(temp_file, 'wb') as wav_out:
        wav_out.setnchannels(channels)
        wav_out.setsampwidth(sample_width)
        wav_out.setframerate(framerate)
        wav_out.writeframes(frames1)
        wav_out.writeframes(frames2)

    # 将临时文件重命名为第一个 wav 文件的名称
    shutil.move(temp_file, file1)


def wait_input():
    global flag_text
    while True:
        if flag_text:
            break


def input_text(text):
    global source_text
    global flag_text
    if text:
        source_text = text
        flag_text = True


def wait_generate():
    global flag_generate, flag_fast_generate
    while True:
        if flag_generate:
            break
        if flag_fast_generate:
            break
        # if flag_fast_generate:
        #     break


def generate_audio(item):
    global flag_text, flag_generate, flag_fast_generate, source_text
    if not flag_fast_generate:
        if item:
            flag_text = True
            flag_generate = True
            source_text = item
    else:
        print("正在快速合成！")


def generate_audio_fast(item):
    global flag_text, flag_generate, flag_fast_generate, source_text
    if not flag_generate:
        if item:
            flag_text = True
            flag_fast_generate = True
            source_text = item
    else:
        print("正在合成！")


def terminate_tts():
    global flag_text, flag_terminate
    flag_terminate = True
    flag_text = True


def speech_synthesis(model_dir):
    print('Lemon4> Begin speech synthesis!')
    vits_path = os.path.join(model_dir, 'pretrained_model.pth')
    config_path = os.path.join(model_dir, 'config.json')
    print('Lemon4> Loading models...')
    hps = utils.get_hparams_from_file(config_path)
    vits = Vits(vits_path, hps, device)
    print('Lemon4> Successfully loaded models!')

    while True:
        global flag_text, flag_generate, flag_fast_generate, flag_terminate, source_text
        flag_text = flag_generate = flag_terminate = False

        print('Lemon4> Please input some text...')
        wait_input()

        if flag_terminate:
            print('Lemon4> Terminating...')
            break

        wait_generate()
        if flag_generate:
            print('Lemon4> Generating (normal mode)...')
            try:
                vits.inference(source_text)
                print('Lemon4> Successfully synthesized speech from text!')
            except Exception as e:
                print(e)
            flag_generate = False
        if flag_fast_generate:
            print('Lemon4> Generating (fast mode)...')
            try:
                vits.inference_fast(source_text)
                print('Lemon4> Efficiently synthesized speech from text!')
            except Exception as e:
                print(e)
            flag_fast_generate = False


def play_audio(filename):
    # 打开音频文件
    wf = wave.open(filename, 'rb')

    # 创建 PyAudio 对象
    p = pyaudio.PyAudio()

    # 打开音频输出流
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # 播放音频数据
    data = wf.readframes(1024)
    while data:
        stream.write(data)
        data = wf.readframes(1024)

    # 关闭音频输出流和 PyAudio 对象
    stream.stop_stream()
    stream.close()
    p.terminate()


if __name__ == "__main__":
    # debug use

    model_dir = '../vits/vits_backend'  # 模型文件夹路径
    source_text = '旅行者你好，我是用于测试用的夜之城传奇！'  # 源音频路径
    source_text_fast = '综上，关于益生菌在特应性皮炎治疗中的应用仍存争议。在进一步研究之前，给患儿益生菌作为预防和治疗手段需谨慎。尽管部分研究显示益生菌疗效显著，但仍需更多临床试验和研究以证实有效性和安全性。希望未来有更多的临床研究能为特应性皮炎的预防和治疗提供确切指导。'
    vits_path = '../vits/vits_backend/pretrained_model.pth'
    config_path = '../vits/vits_backend/config.json'
    save_path = '../../cache/vits_generated.wav'
    tmp_path = '../../cache/vits_tmp.wav'
    fast_path = '../../cache/vits_fast_generated.wav'
    play_path = '../../cache/vits_play.wav'
    download_path = '../../cache/vits_download.wav'
    hps = utils.get_hparams_from_file(config_path)
    vits = Vits(vits_path, hps, device, vits_path, play_path, save_path, tmp_path, fast_path)

    # vits.inference(source_text)  # 生成音频放在../../cache中

    vits.inference_fast(source_text_fast)  # 生成音频放在../../cache中