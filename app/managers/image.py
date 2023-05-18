import sys
sys.path.append('../backend/swinir')

from PyQt5.QtCore import QObject, QUrl, QTimer, QFileSystemWatcher
from PyQt5.QtWidgets import QApplication, QGraphicsView, QWidget, QSlider, QFileDialog
from PySide2.QtCore import QRectF
from PySide2.QtWidgets import QGraphicsScene, QGraphicsItem, QVBoxLayout
from PySide2.QtGui import QPixmap, Qt

from app.backend.swinir.inference import load_image
from app.backend.swinir.inference import generate_image


cache_path = 'C:/Users/25402/Desktop/GIT_upload/project8853-288/app/cache/swinir_display.png'
class SliderImageItem(QGraphicsItem):
    def __init__(self, img1, img2):
        super().__init__()

        self.img1 = QPixmap(img1)
        self.img2 = QPixmap(img2)
        self.img2 = self.img2.scaled(self.img1.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.clip = self.img1.width() // 2

    def setClip(self, clip):
        self.clip = clip
        self.update()

    def boundingRect(self):
        return QRectF(self.img1.rect())

    def paint(self, painter, option, widget=None):
        painter.drawPixmap(0, 0, self.img1, 0, 0, self.clip, self.img1.height())
        painter.drawPixmap(self.clip, 0, self.img2, self.clip, 0, self.img2.width() - self.clip, self.img2.height())


class ImageManager(QObject):
    def __init__(self, app):
        super().__init__()
        self._app = app
        self.watcher = QFileSystemWatcher()
        self.watcher.fileChanged.connect(self._file_updated)

    def initialize(self):
        ui = self._app.ui
        self.slider = ui.Image_Slider
        self.view = ui.Image_graphicsView
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)
        self.file_path = None
        ui.Image_pushButton_Upload.clicked.connect(lambda: self._choose_file_path())
        ui.Image_pushButton_StartRepairing.clicked.connect(lambda: self._start_repairing())

    def _choose_file_path(self):
        self.file_path = QFileDialog.getOpenFileName(None, 'Choose a file', '/home')
        load_image(self.file_path[0])
        self.image_item = SliderImageItem(self.file_path[0], self.file_path[0])
        self.scene.addItem(self.image_item)
        self.view.fitInView(self.image_item, Qt.KeepAspectRatio)


    def _start_repairing(self):
        generate_image()
        # self.scene.removeItem(self.image_item)
        self.watcher.addPath(cache_path)

    def _file_updated(self):
        self.scene.removeItem(self.image_item)
        self._set_current_display(self.file_path[0], cache_path)

    def _set_current_display(self, img1, img2):

        self.slider.setRange(0, QPixmap(img1).width())
        self.slider.setValue(QPixmap(img1).width() // 2)

        self.image_item = SliderImageItem(img1, img2)
        self.scene.addItem(self.image_item)
        self.view.fitInView(self.image_item, Qt.KeepAspectRatio)

        self.slider.valueChanged.connect(self.image_item.setClip)


if __name__ == '__main__':
    pass