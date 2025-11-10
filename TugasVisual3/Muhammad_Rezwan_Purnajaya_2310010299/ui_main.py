# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(420, 360)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnGapoktan = QPushButton(self.centralwidget)
        self.btnGapoktan.setObjectName(u"btnGapoktan")

        self.verticalLayout.addWidget(self.btnGapoktan)

        self.btnPoktan = QPushButton(self.centralwidget)
        self.btnPoktan.setObjectName(u"btnPoktan")

        self.verticalLayout.addWidget(self.btnPoktan)

        self.btnPetani = QPushButton(self.centralwidget)
        self.btnPetani.setObjectName(u"btnPetani")

        self.verticalLayout.addWidget(self.btnPetani)

        self.btnPenyuluh = QPushButton(self.centralwidget)
        self.btnPenyuluh.setObjectName(u"btnPenyuluh")

        self.verticalLayout.addWidget(self.btnPenyuluh)

        self.btnLokasi = QPushButton(self.centralwidget)
        self.btnLokasi.setObjectName(u"btnLokasi")

        self.verticalLayout.addWidget(self.btnLokasi)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.btnGapoktan.setText(QCoreApplication.translate("MainWindow", u"Gapoktan", None))
        self.btnPoktan.setText(QCoreApplication.translate("MainWindow", u"Poktan", None))
        self.btnPetani.setText(QCoreApplication.translate("MainWindow", u"Petani", None))
        self.btnPenyuluh.setText(QCoreApplication.translate("MainWindow", u"Penyuluh", None))
        self.btnLokasi.setText(QCoreApplication.translate("MainWindow", u"Lokasi", None))
    # retranslateUi

