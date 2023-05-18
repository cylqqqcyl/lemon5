from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtMultimedia
import sys

sys.path.append('../frontend')
sys.path.append('../backend/sovits')
sys.path.append('../backend/cleanunet')
sys.path.append('../backend/swinir')
sys.path.append('../backend/vits/vits_backend')
sys.path.append('../backend/vits')

from app.frontend.base_win import MainWindow
from app.backend.sovits.inference import convert_audio
from app.backend.cleanunet.inference import denoise_audio
from app.backend.swinir.inference import generate_image
from app.backend.vits.inference import generate_audio, generate_audio_fast


class ConvertManager(QObject):
    """集中管理音频和图片的合成/转换"""

    def __init__(self, app):
        super().__init__()
        self._app = app
        self.text = ""

    def initialize(self):
        """将各个转换功能控件与后端连接"""
        ui = self._app.ui

        # speech enhancement (cleanunet)
        ui.Denoise_pushButton_StartDenoising.clicked.connect(denoise_audio)

        # voice conversion (sovits)
        ui.VC_pushButton_StartConversion.clicked.connect(convert_audio)

        # text-to-speech (vits)
        ui.TTS_textEdit_Text.textChanged.connect(self.getText)
        ui.TTS_pushButton_GenerateSpeech.clicked.connect(lambda: generate_audio(self.text))
        ui.TTS_pushButton_FastGenerate.clicked.connect(lambda: generate_audio_fast(self.text))
        # # super resolution (swinir)
        ui.Image_pushButton_StartRepairing.clicked.connect(generate_image)


    def getText(self):
        # 获取 QTextEdit 中的文本
        self.text = self._app.ui.TTS_textEdit_Text.toPlainText()
        print(self.text)

