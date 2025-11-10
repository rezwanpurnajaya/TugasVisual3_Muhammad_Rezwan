# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gapoktanForm.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_GapoktanForm(object):
    def setupUi(self, GapoktanForm):
        if not GapoktanForm.objectName():
            GapoktanForm.setObjectName(u"GapoktanForm")
        GapoktanForm.resize(500, 380)
        self.verticalLayout = QVBoxLayout(GapoktanForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lblId = QLabel(GapoktanForm)
        self.lblId.setObjectName(u"lblId")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblId)

        self.id_gapoktan = QSpinBox(GapoktanForm)
        self.id_gapoktan.setObjectName(u"id_gapoktan")
        self.id_gapoktan.setEnabled(False)
        self.id_gapoktan.setMaximum(2147483647)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.id_gapoktan)

        self.lblNama = QLabel(GapoktanForm)
        self.lblNama.setObjectName(u"lblNama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblNama)

        self.nama_gapoktan = QLineEdit(GapoktanForm)
        self.nama_gapoktan.setObjectName(u"nama_gapoktan")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.nama_gapoktan)

        self.lblKetua = QLabel(GapoktanForm)
        self.lblKetua.setObjectName(u"lblKetua")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblKetua)

        self.ketua = QLineEdit(GapoktanForm)
        self.ketua.setObjectName(u"ketua")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.ketua)

        self.lblKontak = QLabel(GapoktanForm)
        self.lblKontak.setObjectName(u"lblKontak")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblKontak)

        self.kontak = QLineEdit(GapoktanForm)
        self.kontak.setObjectName(u"kontak")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.kontak)

        self.lblIdLokasi = QLabel(GapoktanForm)
        self.lblIdLokasi.setObjectName(u"lblIdLokasi")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblIdLokasi)

        self.id_lokasi = QLineEdit(GapoktanForm)
        self.id_lokasi.setObjectName(u"id_lokasi")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.id_lokasi)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnSave = QPushButton(GapoktanForm)
        self.btnSave.setObjectName(u"btnSave")

        self.buttonLayout.addWidget(self.btnSave)

        self.btnClear = QPushButton(GapoktanForm)
        self.btnClear.setObjectName(u"btnClear")

        self.buttonLayout.addWidget(self.btnClear)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer)

        self.btnClose = QPushButton(GapoktanForm)
        self.btnClose.setObjectName(u"btnClose")

        self.buttonLayout.addWidget(self.btnClose)


        self.verticalLayout.addLayout(self.buttonLayout)


        self.retranslateUi(GapoktanForm)

        QMetaObject.connectSlotsByName(GapoktanForm)
    # setupUi

    def retranslateUi(self, GapoktanForm):
        GapoktanForm.setWindowTitle(QCoreApplication.translate("GapoktanForm", u"Form Gapoktan (Sederhana)", None))
        self.lblId.setText(QCoreApplication.translate("GapoktanForm", u"ID Gapoktan", None))
        self.lblNama.setText(QCoreApplication.translate("GapoktanForm", u"Nama", None))
        self.lblKetua.setText(QCoreApplication.translate("GapoktanForm", u"Ketua", None))
        self.lblKontak.setText(QCoreApplication.translate("GapoktanForm", u"Kontak", None))
        self.lblIdLokasi.setText(QCoreApplication.translate("GapoktanForm", u"ID Lokasi", None))
        self.btnSave.setText(QCoreApplication.translate("GapoktanForm", u"Simpan", None))
        self.btnClear.setText(QCoreApplication.translate("GapoktanForm", u"Bersihkan", None))
        self.btnClose.setText(QCoreApplication.translate("GapoktanForm", u"Tutup", None))
    # retranslateUi

