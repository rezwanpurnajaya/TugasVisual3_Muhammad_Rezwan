# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PoktanForm.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_PoktanForm(object):
    def setupUi(self, PoktanForm):
        if not PoktanForm.objectName():
            PoktanForm.setObjectName(u"PoktanForm")
        PoktanForm.resize(500, 380)
        self.verticalLayout = QVBoxLayout(PoktanForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lblId = QLabel(PoktanForm)
        self.lblId.setObjectName(u"lblId")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblId)

        self.id_poktan = QSpinBox(PoktanForm)
        self.id_poktan.setObjectName(u"id_poktan")
        self.id_poktan.setEnabled(False)
        self.id_poktan.setMaximum(2147483647)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.id_poktan)

        self.lblNama = QLabel(PoktanForm)
        self.lblNama.setObjectName(u"lblNama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblNama)

        self.nama_poktan = QLineEdit(PoktanForm)
        self.nama_poktan.setObjectName(u"nama_poktan")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.nama_poktan)

        self.lblKetua = QLabel(PoktanForm)
        self.lblKetua.setObjectName(u"lblKetua")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblKetua)

        self.ketua = QLineEdit(PoktanForm)
        self.ketua.setObjectName(u"ketua")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.ketua)

        self.lblKelas = QLabel(PoktanForm)
        self.lblKelas.setObjectName(u"lblKelas")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblKelas)

        self.kelas = QComboBox(PoktanForm)
        self.kelas.addItem("")
        self.kelas.addItem("")
        self.kelas.addItem("")
        self.kelas.setObjectName(u"kelas")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.kelas)

        self.lblIdGapoktan = QLabel(PoktanForm)
        self.lblIdGapoktan.setObjectName(u"lblIdGapoktan")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblIdGapoktan)

        self.id_gapoktan = QLineEdit(PoktanForm)
        self.id_gapoktan.setObjectName(u"id_gapoktan")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.id_gapoktan)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnSave = QPushButton(PoktanForm)
        self.btnSave.setObjectName(u"btnSave")

        self.buttonLayout.addWidget(self.btnSave)

        self.btnClear = QPushButton(PoktanForm)
        self.btnClear.setObjectName(u"btnClear")

        self.buttonLayout.addWidget(self.btnClear)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer)

        self.btnClose = QPushButton(PoktanForm)
        self.btnClose.setObjectName(u"btnClose")

        self.buttonLayout.addWidget(self.btnClose)


        self.verticalLayout.addLayout(self.buttonLayout)


        self.retranslateUi(PoktanForm)

        QMetaObject.connectSlotsByName(PoktanForm)
    # setupUi

    def retranslateUi(self, PoktanForm):
        PoktanForm.setWindowTitle(QCoreApplication.translate("PoktanForm", u"Form Poktan (Sederhana)", None))
        self.lblId.setText(QCoreApplication.translate("PoktanForm", u"ID Poktan", None))
        self.lblNama.setText(QCoreApplication.translate("PoktanForm", u"Nama", None))
        self.lblKetua.setText(QCoreApplication.translate("PoktanForm", u"Ketua", None))
        self.lblKelas.setText(QCoreApplication.translate("PoktanForm", u"Kelas", None))
        self.kelas.setItemText(0, QCoreApplication.translate("PoktanForm", u"Pemula", None))
        self.kelas.setItemText(1, QCoreApplication.translate("PoktanForm", u"Madya", None))
        self.kelas.setItemText(2, QCoreApplication.translate("PoktanForm", u"Utama", None))

        self.lblIdGapoktan.setText(QCoreApplication.translate("PoktanForm", u"ID Gapoktan", None))
        self.btnSave.setText(QCoreApplication.translate("PoktanForm", u"Simpan", None))
        self.btnClear.setText(QCoreApplication.translate("PoktanForm", u"Bersihkan", None))
        self.btnClose.setText(QCoreApplication.translate("PoktanForm", u"Tutup", None))
    # retranslateUi

