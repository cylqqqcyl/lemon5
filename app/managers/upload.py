from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

sys.path.append('../frontend')
sys.path.append('../backend/sovits')
sys.path.append('../backend/cleanunet')
sys.path.append('../backend/swinir')

from app.frontend.base_win import MainWindow
from app.backend.sovits.inference import load_audio as load_audio_vc
from app.backend.cleanunet.inference import load_audio as load_audio_se
from app.backend.swinir.inference import load_image
from app.backend.vits.inference import input_text

class UploadManager(QObject):
    def __init__(self, app):
        super().__init__()
        self._app = app

    def initialize(self):
        ui = self._app.ui
        # speech enhancement (cleanunet)
        ui.Denoise_pushButton_SelectFile.clicked.connect(lambda: self._choose_file_path('se'))
        # voice conversion (sovits)
        ui.VC_pushButton_Upload.clicked.connect(lambda: self._choose_file_path('vc'))
        # super resolution (swinir)
        # ui.Image_pushButton_Upload.clicked.connect(lambda: self._choose_file_path('sr'))


    def _choose_file_path(self, model_type):
        file_path = QFileDialog.getOpenFileName(None, 'Choose a file', '/home')
        if file_path[0]:
            if model_type == 'vc':
                self._app.play_path_vc_before = file_path[0]
                load_audio_vc(file_path[0])
            elif model_type == 'se':
                self._app.play_path_se_before = file_path[0]
                load_audio_se(file_path[0])
            # elif model_type == 'sr':
            #     load_image(file_path[0])
            else:
                raise TypeError(f'No such model type: {model_type}!')
