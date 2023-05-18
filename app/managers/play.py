from PyQt5.QtCore import QObject, QUrl, QTimer
from PyQt5 import QtMultimedia
import traceback


class PlayManager(QObject):
    def __init__(self, app):
        super().__init__()
        self._app = app
        self._player_vc_before = QtMultimedia.QMediaPlayer()
        self._player_vc_after = QtMultimedia.QMediaPlayer()
        self._player_tts = QtMultimedia.QMediaPlayer()
        self._player_se_before = QtMultimedia.QMediaPlayer()
        self._player_se_after = QtMultimedia.QMediaPlayer()
        self._player_vc_before.setVolume(50)
        self._player_se_after.setVolume(50)
        self._player_tts.setVolume(50)
        self._player_se_before.setVolume(50)
        self._player_se_after.setVolume(50)

        self._timer_vc_before = QTimer()
        self._timer_vc_after = QTimer()
        self._timer_tts = QTimer()
        self._timer_se_before = QTimer()
        self._timer_se_after = QTimer()

        self._is_playing_vc_before = False
        self._is_playing_vc_after = False
        self._is_playing_tts = False
        self._is_playing_se_before = False
        self._is_playing_se_after = False

    def initialize(self):
        self._timer_vc_before.start(1000)
        self._timer_vc_after.start(1000)
        self._timer_se_before.start(1000)
        self._timer_se_after.start(1000)
        self._timer_tts.start(1000)

        self._app.ui.VC_pushButton_PlayAudio_before.clicked.connect(lambda: self._play_audio('vc_before'))
        self._timer_vc_before.timeout.connect(lambda: self._update_slider('vc_before'))

        self._app.ui.VC_pushButton_PlayAudio_after.clicked.connect(lambda: self._play_audio('vc_before'))
        self._timer_vc_after.timeout.connect(lambda: self._update_slider('vc_before'))

        self._app.ui.Denoise_pushButton_PlayAudio_before.clicked.connect(lambda: self._play_audio('se_before'))
        self._timer_se_before.timeout.connect(lambda: self._update_slider('se_before'))

        self._app.ui.Denoise_pushButton_PlayAudio_after.clicked.connect(lambda: self._play_audio('se_after'))
        self._timer_se_after.timeout.connect(lambda: self._update_slider('se_after'))

        self._app.ui.TTS_pushButton_PlayAudio.clicked.connect(lambda: self._play_audio('tts'))
        self._timer_tts.timeout.connect(lambda: self._update_slider('tts'))

    def _set_current_playing(self, model_type):
        if model_type == 'vc_before':
            try:
                path = self._app.play_path_vc_before
                content = QtMultimedia.QMediaContent(QUrl.fromLocalFile(path))
                self._player_vc_before.setMedia(content)
            except:
                print('Nothing to play!')

        elif model_type == 'vc_after':
            try:
                path = self._app.play_path_vc_after
                content = QtMultimedia.QMediaContent(QUrl.fromLocalFile(path))
                self._player_vc_after.setMedia(content)
            except:
                print('Nothing to play!')

        elif model_type == 'se_before':
            try:
                path = self._app.play_path_se_before
                content = QtMultimedia.QMediaContent(QUrl.fromLocalFile(path))
                self._player_se_before.setMedia(content)
            except:
                print('Nothing to play!')

        elif model_type == 'se_after':
            try:
                path = self._app.play_path_se_after
                content = QtMultimedia.QMediaContent(QUrl.fromLocalFile(path))
                self._player_se_after.setMedia(content)
            except:
                print('Nothing to play!')

        elif model_type == 'tts':
            try:
                path = self._app.play_path_tts
                content = QtMultimedia.QMediaContent(QUrl.fromLocalFile(path))
                self._player_tts.setMedia(content)
            except:
                print('Nothing to play!')
        else:
            raise TypeError(f'No such model type: {model_type}!')

    def _play_audio(self, model_type):
        if model_type == 'vc_before':
            if not self._player_vc_before.isAudioAvailable():
                self._set_current_playing(model_type)
            if not self._is_playing_vc_before:
                # self._app.ui.VC_pushButton_StartConversion.setDisable(True)
                self._is_playing_vc_before = True
                self._player_vc_before.play()
            else:
                self._is_playing_vc_before = False
                # TODO: 需要跟新play按钮的icon
                self._player_vc_before.pause()

        elif model_type == 'vc_after':
            if not self._player_vc_after.isAudioAvailable():
                self._set_current_playing(model_type)
            if not self._is_playing_vc_after:
                self._app.ui.VC_pushButton_StartConversion.setDisable(True)
                self._is_playing_vc_after = True
                self._player_vc_after.play()
            else:
                self._is_playing_vc_after = False
                # TODO: 需要跟新play按钮的icon
                self._player_vc_after.pause()

        elif model_type == 'tts':
            if not self._player_tts.isAudioAvailable():
                self._set_current_playing(model_type)
            if not self._is_playing_tts:
                # self._app.ui.Denoise_pushButton_StartDenoising.setDisable(True)
                self._is_playing_tts = True
                self._player_tts.play()
            else:
                self._is_playing_tts = False
                # TODO: 需要跟新play按钮的icon
                self._player_tts.pause()

        elif model_type == 'se_before':
            if not self._player_se_before.isAudioAvailable():
                self._set_current_playing(model_type)
            if not self._is_playing_se_before:
                # self._app.ui.Denoise_pushButton_StartDenoising.setDisable(True)
                self._is_playing_se_before = True
                self._player_se_before.play()
            else:
                self._is_playing_se_before = False
                # TODO: 需要跟新play按钮的icon
                self._player_se_before.pause()

        elif model_type == 'se_after':
            if not self._player_se_after.isAudioAvailable():
                self._set_current_playing(model_type)
            if not self._is_playing_se_after:
                self._app.ui.Denoise_pushButton_StartDenoising.setDisable(True)
                self._is_playing_se_after = True
                self._player_se_after.play()
            else:
                self._is_playing_se_after = False
                # TODO: 需要跟新play按钮的icon
                self._player_se_after.pause()

        else:
            raise TypeError(f'No such model type: {model_type}!')

    def _update_slider(self, model_type):
        if model_type == 'vc_before':
            if self._is_playing_vc_before:
                self._app.ui.VC_Slider_before.setMinimum(0)
                self._app.ui.VC_Slider_before.setMaximum(self._player_vc_before.duration())
                self._app.ui.VC_Slider_before.setValue(self._app.ui.VC_Slider_before.value() + 1000)

            if self._player_vc_before.position() == self._player_vc_before.duration():
                self._app.ui.VC_Slider_before.setValue(0)
                self._is_playing_vc_before = False
                self._player_vc_before.stop()
                # TODO: 更新play button

        elif model_type == 'vc_after':
            if self._is_playing_vc_after:
                self._app.ui.VC_Slider_after.setMinimum(0)
                self._app.ui.VC_Slider_after.setMaximum(self._player_vc_after.duration())
                self._app.ui.VC_Slider_after.setValue(self._app.ui.VC_Slider_after.value() + 1000)

            if self._player_vc_after.position() == self._player_vc_after.duration():
                self._app.ui.VC_Slider_after.setValue(0)
                self._is_playing_vc_after = False
                self._player_vc_after.stop()
                # TODO: 更新play button

        elif model_type == 'tts':
            if self._is_playing_tts:
                self._app.ui.TTS_Slider.setMinimum(0)
                self._app.ui.TTS_Slider.setMaximum(self._player_tts.duration())
                self._app.ui.TTS_Slider.setValue(self._app.ui.TTS_Slider.value() + 1000)

            if self._player_tts.position() == self._player_tts.duration():
                self._app.ui.TTS_Slider.setValue(0)
                self._is_playing_tts = False
                self._player_tts.stop()
                # TODO: 更新play button

        elif model_type == 'se_before':
            if self._is_playing_se_before:
                self._app.ui.Denoise_Slider_before.setMinimum(0)
                self._app.ui.Denoise_Slider_before.setMaximum(self._player_se_before.duration())
                self._app.ui.Denoise_Slider_before.setValue(self._app.ui.Denoise_Slider_before.value() + 1000)

            if self._player_se_before.position() == self._player_se_before.duration():
                self._app.ui.Denoise_Slider_before.setValue(0)
                self._is_playing_se_before = False
                self._player_se_before.stop()
                # TODO: 更新play button

        elif model_type == 'se_after':
            if self._is_playing_se_after:
                self._app.ui.Denoise_Slider_after.setMinimum(0)
                self._app.ui.Denoise_Slider_after.setMaximum(self._player_se_after.duration())
                self._app.ui.Denoise_Slider_after.setValue(self._app.ui.Denoise_Slider_after.value() + 1000)

            if self._player_se_after.position() == self._player_se_after.duration():
                self._app.ui.Denoise_Slider_after.setValue(0)
                self._is_playing_se_after = False
                self._player_se_after.stop()
                # TODO: 更新play button

        else:
            raise TypeError(f'No such model type: {model_type}!')
