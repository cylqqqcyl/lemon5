from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import threading

sys.path.append('../frontend')
sys.path.append('../backend/sovits')
sys.path.append('../backend/cleanunet')
sys.path.append('../backend/swinir')
sys.path.append('../backend/vits')

from app.frontend.base_win import MainWindow
from app.backend.sovits.inference import voice_conversion, terminate_vc, select_speaker
from app.backend.cleanunet.inference import denoising, terminate_se
from app.backend.swinir.inference import super_resolution, terminate_sr
from app.backend.vits.inference import speech_synthesis, terminate_tts
from app.managers.misc import get_model_info


class ModelManager(QObject):
    def __init__(self, app):
        super().__init__()
        self._app = app
        self.model_dir_tts = None
        self.model_dir_vc = None
        self.model_dir_se = None
        self.model_dir_sr = None

        # 加载模型的线程
        self.thread_model_vc = None
        self.thread_model_se = None
        self.thread_model_sr = None
        self.thread_model_tts = None


    def initialize(self):
        ui = self._app.ui

        # speech enhancement (cleanunet)
        ui.Denoise_pushButton_SelectTheModel.clicked.connect(lambda: self._choose_model_dir('se'))
        ui.Denoise_pushButton_StartLoading.clicked.connect(lambda: self._load_model('se'))
        # voice conversion (sovits)
        ui.VC_pushButton_SelectTheModel.clicked.connect(lambda: self._choose_model_dir('vc'))
        ui.VC_pushButton_StartLoading.clicked.connect(lambda: self._load_model('vc'))
        ui.VC_comboBox_SelectRole.currentIndexChanged.connect(lambda: select_speaker(ui.VC_comboBox_SelectRole.currentIndex()))
        # text-to-speech (vits)
        ui.TTS_pushButton_SelcetTheModel.clicked.connect(lambda: self._choose_model_dir('tts'))
        ui.TTS_pushButton_StartLoading.clicked.connect(lambda: self._load_model('tts'))
        ui.TTS_comboBox_SelectRole.currentIndexChanged.connect(lambda: select_speaker(ui.TTS_comboBox_SelectRole.currentIndex()))
        # super resolution (swinir)
        ui.Image_pushButton_SelectTheModel.clicked.connect(lambda: self._choose_model_dir('sr'))
        ui.Image_pushButton_StartLoading.clicked.connect(lambda: self._load_model('sr'))

    def _choose_model_dir(self, model_type):
        dir_path = QFileDialog.getExistingDirectory(None, 'Choose a model directory', '/home')
        if dir_path:
            if model_type == 'tts':
                self.model_dir_tts = dir_path
                self._app.ui.model_path_tts_edit.setText(dir_path)
            if model_type == 'vc':
                self.model_dir_vc = dir_path
                self._app.ui.model_path_vc_edit.setText(dir_path)
            elif model_type == 'se':
                self.model_dir_se = dir_path
                self._app.ui.model_path_se_edit.setText(dir_path)
            elif model_type == 'sr':
                self.model_dir_sr = dir_path
                self._app.ui.model_path_sr_edit.setText(dir_path)
            else:
                raise TypeError(f'No such model type: {model_type}!')

    def _load_model(self, model_type):
        ui = self._app.ui

        if model_type == 'tts':
            if self.model_dir_tts:
                while self.thread_model_tts and self.thread_model_tts.is_alive():
                    terminate_tts()
                self.thread_model_tts = threading.Thread(target=speech_synthesis,
                                                        args=[self.model_dir_tts])
                self.thread_model_tts.setDaemon(True)
                self.thread_model_tts.start()
                model_info = get_model_info(self.model_dir_tts)
                # model_name = model_info.info.model_name
                # speakers = model_info.info.speakers
                ui.TTS_comboBox_SelectRole.clear()
                # for speaker in speakers:
                #     ui.TTS_comboBox_SelectRole.addItem(speaker)
                # if len(speakers) == 1:
                #     ui.TTS_comboBox_SelectRole.setDisabled(True)
                # else:
                #     ui.TTS_comboBox_SelectRole.setDisabled(False)
            else:
                QMessageBox.information(None,
                                        'Information',
                                        'Please choose a model directory first!')
        elif model_type == 'vc':
            if self.model_dir_vc:
                while self.thread_model_vc and self.thread_model_vc.is_alive():
                    terminate_vc()
                self.thread_model_vc = threading.Thread(target=voice_conversion,
                                                        args=[self.model_dir_vc])
                self.thread_model_vc.setDaemon(True)
                self.thread_model_vc.start()
                model_info = get_model_info(self.model_dir_vc)
                # model_name = model_info.info.model_name
                speakers = model_info.info.speakers
                ui.VC_comboBox_SelectRole.clear()
                for speaker in speakers:
                    ui.VC_comboBox_SelectRole.addItem(speaker)
                if len(speakers) == 1:
                    ui.VC_comboBox_SelectRole.setDisabled(True)
                else:
                    ui.VC_comboBox_SelectRole.setDisabled(False)

            else:
                QMessageBox.information(None,
                                        'Information',
                                        'Please choose a model directory first!')
        elif model_type == 'se':
            if self.model_dir_se:
                while self.thread_model_se and self.thread_model_se.is_alive():
                    terminate_se()
                self.thread_model_se = threading.Thread(target=denoising,
                                                        args=[self.model_dir_se])
                self.thread_model_se.setDaemon(True)
                self.thread_model_se.start()
            else:
                QMessageBox.information(None,
                                        'Information',
                                        'Please choose a model directory first!')
        elif model_type == 'sr':
            if self.model_dir_sr:
                while self.thread_model_sr and self.thread_model_sr.is_alive():
                    terminate_sr()
                self.thread_model_sr = threading.Thread(target=super_resolution,
                                                        args=[self.model_dir_sr])
                self.thread_model_sr.setDaemon(True)
                self.thread_model_sr.start()
            else:
                QMessageBox.information(None,
                                        'Information',
                                        'Please choose a model directory first!')
        else:
            raise TypeError(f'No such model type: {model_type}!')

    def _terminate_inference(self, model_type):
        """结束当前模型推理线程"""
        if model_type == 'tts':
            terminate_tts()
        elif model_type == 'vc':
            terminate_vc()
        elif model_type == 'se':
            terminate_se()
        elif model_type == 'sr':
            terminate_sr()
        else:
            raise TypeError(f'No such model type: {model_type}!')
