import threading
import wave
import os
import shutil
import time
import pyaudio
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtMultimedia
import sys
import threading

sys.path.append('frontend')
sys.path.append('backend/sovits')
sys.path.append('backend/cleanunet')
sys.path.append('backend/swinir')
sys.path.append('backend/vits/vits_backend')
sys.path.append('backend/vits')

from managers.misc import EmitStr

from frontend.base_win import MainWindow
# import backend.cleanunet.inference as CleanUNet
# import backend.swinir.inference as SwinIR
# import backend.sovits.inference as Sovits
from managers.model import ModelManager
from managers.upload import UploadManager
from managers.convert import ConvertManager
from managers.download import DownloadManager
from managers.info import InfoManager
from managers.play import PlayManager
from managers.image import ImageManager

# vits


class Lemon4UI(MainWindow):
    def __init__(self):
        super(Lemon4UI, self).__init__()
        self.emit_str_info = EmitStr()
        self.emit_str_error = EmitStr()

        # 不得已为之……
        self.play_path_vc_before = None
        self.play_path_vc_after = 'cache/sovits_play.wav'
        self.play_path_tts = None  # TODO
        self.play_path_se_before = None
        self.play_path_se_after = 'cache/denoise_play.wav'

    def closeEvent(self, e):
        self.dialogexec('Question', "Are you sure to close Lemon4?", "icons/1x/errorAsset 55.png", "Yes", "Cancel")
        if self.diag.reply_west:
            e.accept()
        else:
            e.ignore()


class Lemon4:
    def __init__(self):
        self.app = Lemon4UI()
        self.load_mgr = ModelManager(self.app)
        self.upload_mgr = UploadManager(self.app)
        self.convert_mgr = ConvertManager(self.app)
        self.download_mgr = DownloadManager(self.app)
        self.info_mgr = InfoManager(self.app)
        self.play_mgr = PlayManager(self.app)
        self.image_mgr = ImageManager(self.app)
        self.initialize()

    def initialize(self):
        self.load_mgr.initialize()
        self.upload_mgr.initialize()
        self.convert_mgr.initialize()
        self.download_mgr.initialize()
        self.info_mgr.initialize()
        self.play_mgr.initialize()
        self.image_mgr.initialize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lemon = Lemon4()
    print('Welcome to Lemon4!')
    lemon.app.show()
    sys.exit(app.exec_())
