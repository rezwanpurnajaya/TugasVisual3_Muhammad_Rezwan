# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from Lokasi import form_lokasi
from Gapoktan import form_gapoktan
from Poktan import form_poktan
from Petani import form_petani
from Penyuluh import form_penyuluh


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya = QFile("form.ui")
        filenya.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formutama = loader.load(filenya, self)
        self.resize(self.formutama.size())
        self.setMenuBar(self.formutama.menuBar())

        self.formutama.actionDATA_LOKASI.triggered.connect(self.buka_lokasi)
        self.formutama.actionDATA_GAPOKTAN.triggered.connect(self.buka_gapoktan)
        self.formutama.actionDATA_POKTAN.triggered.connect(self.buka_poktan)
        self.formutama.actionDATA_PETANI.triggered.connect(self.buka_petani)
        self.formutama.actionDATA_PENYULUH.triggered.connect(self.buka_penyuluh)

    def buka_lokasi(self):
        self.fLok = form_lokasi()
        self.fLok.show()

    def buka_gapoktan(self):
        self.fGap = form_gapoktan()
        self.fGap.show()

    def buka_poktan(self):
        self.fPok = form_poktan()
        self.fPok.show()

    def buka_petani(self):
        self.fPet = form_petani()
        self.fPet.show()

    def buka_penyuluh(self):
        self.fPeny = form_penyuluh()
        self.fPeny.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    jendela = MainWindow()
    jendela.show()
    sys.exit(app.exec())
