# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PetaniForm.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_PetaniForm(object):
    def setupUi(self, PetaniForm):
        if not PetaniForm.objectName():
            PetaniForm.setObjectName(u"PetaniForm")
        PetaniForm.resize(500, 380)
        self.verticalLayout = QVBoxLayout(PetaniForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lblId = QLabel(PetaniForm)
        self.lblId.setObjectName(u"lblId")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblId)

        self.id_petani = QSpinBox(PetaniForm)
        self.id_petani.setObjectName(u"id_petani")
        self.id_petani.setEnabled(False)
        self.id_petani.setMaximum(2147483647)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.id_petani)

        self.lblNama = QLabel(PetaniForm)
        self.lblNama.setObjectName(u"lblNama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblNama)

        self.nama = QLineEdit(PetaniForm)
        self.nama.setObjectName(u"nama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.nama)

        self.lblAlamat = QLabel(PetaniForm)
        self.lblAlamat.setObjectName(u"lblAlamat")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblAlamat)

        self.alamat = QLineEdit(PetaniForm)
        self.alamat.setObjectName(u"alamat")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.alamat)

        self.lblKomoditas = QLabel(PetaniForm)
        self.lblKomoditas.setObjectName(u"lblKomoditas")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblKomoditas)

        self.komoditas = QLineEdit(PetaniForm)
        self.komoditas.setObjectName(u"komoditas")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.komoditas)

        self.lblLuas = QLabel(PetaniForm)
        self.lblLuas.setObjectName(u"lblLuas")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblLuas)

        self.luas_lahan = QDoubleSpinBox(PetaniForm)
        self.luas_lahan.setObjectName(u"luas_lahan")
        self.luas_lahan.setDecimals(2)
        self.luas_lahan.setMaximum(1000000.000000000000000)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.luas_lahan)

        self.lblUmur = QLabel(PetaniForm)
        self.lblUmur.setObjectName(u"lblUmur")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblUmur)

        self.umur = QSpinBox(PetaniForm)
        self.umur.setObjectName(u"umur")
        self.umur.setMaximum(150)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.umur)

        self.lblKontak = QLabel(PetaniForm)
        self.lblKontak.setObjectName(u"lblKontak")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.lblKontak)

        self.kontak = QLineEdit(PetaniForm)
        self.kontak.setObjectName(u"kontak")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.kontak)

        self.lblIdPoktan = QLabel(PetaniForm)
        self.lblIdPoktan.setObjectName(u"lblIdPoktan")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.lblIdPoktan)

        self.id_poktan = QLineEdit(PetaniForm)
        self.id_poktan.setObjectName(u"id_poktan")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.id_poktan)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnSave = QPushButton(PetaniForm)
        self.btnSave.setObjectName(u"btnSave")

        self.buttonLayout.addWidget(self.btnSave)

        self.btnClear = QPushButton(PetaniForm)
        self.btnClear.setObjectName(u"btnClear")

        self.buttonLayout.addWidget(self.btnClear)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer)

        self.btnClose = QPushButton(PetaniForm)
        self.btnClose.setObjectName(u"btnClose")

        self.buttonLayout.addWidget(self.btnClose)


        self.verticalLayout.addLayout(self.buttonLayout)


        self.retranslateUi(PetaniForm)

        QMetaObject.connectSlotsByName(PetaniForm)
    # setupUi

    def retranslateUi(self, PetaniForm):
        PetaniForm.setWindowTitle(QCoreApplication.translate("PetaniForm", u"Form Petani (Sederhana)", None))
        self.lblId.setText(QCoreApplication.translate("PetaniForm", u"ID Petani", None))
        self.lblNama.setText(QCoreApplication.translate("PetaniForm", u"Nama", None))
        self.lblAlamat.setText(QCoreApplication.translate("PetaniForm", u"Alamat", None))
        self.lblKomoditas.setText(QCoreApplication.translate("PetaniForm", u"Komoditas", None))
        self.lblLuas.setText(QCoreApplication.translate("PetaniForm", u"Luas Lahan", None))
        self.lblUmur.setText(QCoreApplication.translate("PetaniForm", u"Umur", None))
        self.lblKontak.setText(QCoreApplication.translate("PetaniForm", u"Kontak", None))
        self.lblIdPoktan.setText(QCoreApplication.translate("PetaniForm", u"ID Poktan", None))
        self.btnSave.setText(QCoreApplication.translate("PetaniForm", u"Simpan", None))
        self.btnClear.setText(QCoreApplication.translate("PetaniForm", u"Bersihkan", None))
        self.btnClose.setText(QCoreApplication.translate("PetaniForm", u"Tutup", None))
    # retranslateUi

