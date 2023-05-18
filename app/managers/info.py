from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

from app.managers.misc import EmitStr

class InfoManager(QObject):
    def __init__(self, app):
        super().__init__()
        self._app = app

    def initialize(self):
        # debug时注释掉下面2行
        sys.stdout = EmitStr(textWrite=self.outputWriteInfo)  # redirect stdout
        # sys.stderr = EmitStr(textWrite=self.outputWriteError)  # redirect stderr
        pass

    def outputWriteInfo(self, text):
        self._app.ui.Denoise_textBrowser.append(text)
        self._app.ui.Image_textBrowser.append(text)
        self._app.ui.VC_textBrowser.append(text)
        self._app.ui.TTS_textBrowser.append(text)

    def outputWriteError(self, text):
        self._app.ui.Denoise_textBrowser.append(f'<font color=\'#FF0000\'>{text}</font>')
        self._app.ui.Image_textBrowser.append(f'<font color=\'#FF0000\'>{text}</font>')
        self._app.ui.VC_textBrowser.append(f'<font color=\'#FF0000\'>{text}</font>')
        self._app.ui.TTS_textBrowser.append(f'<font color=\'#FF0000\'>{text}</font>')
