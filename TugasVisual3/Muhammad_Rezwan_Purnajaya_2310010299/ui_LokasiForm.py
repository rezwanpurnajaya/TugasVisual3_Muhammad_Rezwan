# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LokasiForm.ui'
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

class Ui_LokasiForm(object):
    def setupUi(self, LokasiForm):
        if not LokasiForm.objectName():
            LokasiForm.setObjectName(u"LokasiForm")
        LokasiForm.resize(500, 380)
        self.verticalLayout = QVBoxLayout(LokasiForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lblId = QLabel(LokasiForm)
        self.lblId.setObjectName(u"lblId")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblId)

        self.id_lokasi = QSpinBox(LokasiForm)
        self.id_lokasi.setObjectName(u"id_lokasi")
        self.id_lokasi.setEnabled(False)
        self.id_lokasi.setMaximum(2147483647)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.id_lokasi)

        self.lblProv = QLabel(LokasiForm)
        self.lblProv.setObjectName(u"lblProv")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblProv)

        self.provinsi = QLineEdit(LokasiForm)
        self.provinsi.setObjectName(u"provinsi")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.provinsi)

        self.lblKab = QLabel(LokasiForm)
        self.lblKab.setObjectName(u"lblKab")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblKab)

        self.kabupaten = QLineEdit(LokasiForm)
        self.kabupaten.setObjectName(u"kabupaten")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.kabupaten)

        self.lblKec = QLabel(LokasiForm)
        self.lblKec.setObjectName(u"lblKec")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblKec)

        self.kecamatan = QLineEdit(LokasiForm)
        self.kecamatan.setObjectName(u"kecamatan")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.kecamatan)

        self.lblDesa = QLabel(LokasiForm)
        self.lblDesa.setObjectName(u"lblDesa")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblDesa)

        self.desa = QLineEdit(LokasiForm)
        self.desa.setObjectName(u"desa")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.desa)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnSave = QPushButton(LokasiForm)
        self.btnSave.setObjectName(u"btnSave")

        self.buttonLayout.addWidget(self.btnSave)

        self.btnClear = QPushButton(LokasiForm)
        self.btnClear.setObjectName(u"btnClear")

        self.buttonLayout.addWidget(self.btnClear)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer)

        self.btnClose = QPushButton(LokasiForm)
        self.btnClose.setObjectName(u"btnClose")

        self.buttonLayout.addWidget(self.btnClose)


        self.verticalLayout.addLayout(self.buttonLayout)


        self.retranslateUi(LokasiForm)

        QMetaObject.connectSlotsByName(LokasiForm)
    # setupUi

    def retranslateUi(self, LokasiForm):
        LokasiForm.setWindowTitle(QCoreApplication.translate("LokasiForm", u"Form Lokasi (Sederhana)", None))
        self.lblId.setText(QCoreApplication.translate("LokasiForm", u"ID Lokasi", None))
        self.lblProv.setText(QCoreApplication.translate("LokasiForm", u"Provinsi", None))
        self.lblKab.setText(QCoreApplication.translate("LokasiForm", u"Kabupaten", None))
        self.lblKec.setText(QCoreApplication.translate("LokasiForm", u"Kecamatan", None))
        self.lblDesa.setText(QCoreApplication.translate("LokasiForm", u"Desa", None))
        self.btnSave.setText(QCoreApplication.translate("LokasiForm", u"Simpan", None))
        self.btnClear.setText(QCoreApplication.translate("LokasiForm", u"Bersihkan", None))
        self.btnClose.setText(QCoreApplication.translate("LokasiForm", u"Tutup", None))
    # retranslateUi

