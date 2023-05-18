"""
pip install pydub
"""
import sys
import os
sys.path.append('../vits/vits_backend')
sys.path.append('../vits')
# vits_backend_path = os.path.join(os.path.dirname(__file__), "vits_backend")
# sys.path.append(vits_backend_path)
"""
pip install playsound==1.2.2
"""

import multiprocessing
import os
from gtts import gTTS
import time
from vits_backend.vits_infer_api import VitsInfer
import queue
import threading
from playsound import playsound
import re
import sounddevice as sd
import multiprocessing as mp
import queue
import sounddevice as sd
import logging

logger = logging.getLogger('gpt')


def play_sound_0(filenames):
    # Play the resulting audio files in sequence using playsound
    for filename in filenames:
        playsound(filename)

    # Delete the audio files from disk
    # for filename in filenames:
    #    os.remove(filename)


class VitsWrapper:
    def __init__(self, Enable_TTS=True):
        self.vits = VitsInfer()
        self.enable_tts = Enable_TTS
        self.t0 = time.time()
        self.logger = logger

    def generate_audio_slow(self, item):
        if not self.enable_tts:
            self.logger.debug("TTS disabled", flush=True)
            return
        audiopath = self.vits.generate_audio(item)
        self.logger.debug("generate_audio_slow: start playsound")
        playsound(audiopath)

    def generate_audio_thread(self, text_data):
        data_size = len(text_data)
        if not self.enable_tts:
            print("TTS disabled")
            self.audio_queue.put(None)
            self.terminate_event.set()
            return
        for item, filename in text_data:
            # print("generate", item, filename,'\n')
            tmp = self.vits.generate_audio_v2((item, filename))
            # print(type(tmp))
            # time.sleep(0.1)
            self.audio_queue.put(tmp)
        # Add a None value to the queue to indicate the end of audio data
        self.audio_queue.put(None)
        self.complete = True

    def play_sound_x(self):
        while not self.terminate_event.is_set():
            try:
                filename = self.audio_queue.get(timeout=1)
            except queue.Empty:
                time.sleep(1)
                continue
            self.logger.debug("play_sound_x: start")
            playsound(filename)
            if self.complete:
                # self.terminate_event.set()
                return

    def play_sound_y(self, ):
        while not self.terminate_event.is_set():
            try:
                tmp = self.audio_queue.get(timeout=1)
            except queue.Empty:
                time.sleep(0.1)
                continue
            self.logger.debug("play_sound_y: start")
            # Check if we have reached the end of audio data
            if tmp is None:
                self.terminate_event.set()
                break
            if self.complete:
                sd.play(tmp, self.vits.hps.data.sampling_rate)
                sd.wait()
            else:
                sd.play(tmp, self.vits.hps.data.sampling_rate)
                sd.wait()

    def generate_audio_fast(self, new_string):

        text_data_list, filenames = parse(new_string)

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
        # self.cleanup(filenames)

    def cleanup(self, filenames):
        for filename in filenames:
            if os.path.exists(filename):
                try:
                    os.remove(filename)
                    self.logger.debug(f"remove {filename}")
                except OSError as e:
                    self.logger.debug(f"Error deleting file: {e}")
            else:
                self.logger.debug("File does not exist")

    def english_to_chinese(self, text):
        return


def parse(my_string):

    items = re.findall(r'[^。；！？.;!]+[。；！？.;!]', my_string)  # VITS works best when generating whole sentences
    # items = re.split('[^\w]+', my_string)

    while "" in items:
        items.remove("")
    filenames = ["tts2_{}.wav".format(x) for x in range(len(items))]
    text_data_list = list(zip(*[items, filenames]))
    return text_data_list, filenames


if __name__ == "__main__":
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler('sample.log')
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    my_string = "有一天，一只狗在路上遇到了一只猫。狗说：“你好，我叫旺旺，你叫什么？”猫说：“我叫喵喵。”狗说：“喵喵？那是什么名字？你爸爸妈妈都叫什么？”猫说：“我爸爸叫喵星人，我妈妈叫喵咪。”狗说：“那你的祖先呢？”猫说：“我的祖先叫喵祖。”狗说：“喵祖？那是谁？”猫说：“就是我们猫族的始祖，他曾经对人类说过一句话：‘我不是你的奴隶，我是你的主人。’"

    # my_string = "我是人工智能语音助手。我很强我知道！"

    # vits = VitsWrapper()
    # vits.generate_audio_slow(my_string)

    vits = VitsWrapper()
    vits.generate_audio_fast(new_string = my_string)

    # tts = TTS(num_processes=1)
    # tts.tts_output(my_string)
    #
    # tts.start()
    #
    # # add some text to the queue
    # texts, _ = parse(my_string)
    # for text in texts:
    #     tts.speak(text)
    #
    # # stop the TTS system
    # tts.stop()
