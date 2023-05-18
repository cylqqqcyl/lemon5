import shutil

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

sys.path.append('../frontend')
sys.path.append('../backend/sovits')
sys.path.append('../backend/cleanunet')
sys.path.append('../backend/swinir')

from app.frontend.base_win import MainWindow


class DownloadManager(QObject):
    def __init__(self, app):
        super().__init__()
        self._app = app
        self.download_path_vc = '../cache/sovits_download.wav'
        self.download_path_tts = '../cache/vits_download.wav'
        self.download_path_se = '../cache/denoise_download.wav'
        self.download_path_sr = '../cache/swinir_download.png'

    def initialize(self):
        ui = self._app.ui

        # text-to-speech (vits)
        ui.TTS_pushButton_more.clicked.connect(lambda: self._choose_dir_path('tts'))
        # speech enhancement (cleanunet)
        ui.Denoise_pushButton_more.clicked.connect(lambda: self._choose_dir_path('se'))
        # voice conversion (sovits)
        ui.VC_pushButton_more.clicked.connect(lambda: self._choose_dir_path('vc'))
        # super resolution (swinir)
        ui.Image_pushButton_Download.clicked.connect(lambda: self._choose_dir_path('sr'))

    def _choose_dir_path(self, model_type):
        file_path = QFileDialog.getOpenFileName(None, 'Chosse save file path', 'converted.wav', f'(*.wav)')
        if file_path[0]:
            if model_type == 'tts':
                try:
                    shutil.copy(self.download_path_tts, file_path[0])
                except:
                    print('Nothing to download!')
            elif model_type == 'vc':
                try:
                    shutil.copy(self.download_path_vc, file_path[0])
                except:
                    print('Nothing to download!')
            elif model_type == 'se':
                try:
                    shutil.copy(self.download_path_se, file_path[0])
                except:
                    print('Nothing to download!')
            elif model_type == 'sr':
                try:
                    shutil.copy(self.download_path_sr, file_path[0])
                except:
                    print('Nothing to download!')
            else:
                raise TypeError(f'No such model type: {model_type}!')
