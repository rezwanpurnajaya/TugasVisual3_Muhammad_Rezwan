# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PenyuluhForm.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_PenyuluhForm(object):
    def setupUi(self, PenyuluhForm):
        if not PenyuluhForm.objectName():
            PenyuluhForm.setObjectName(u"PenyuluhForm")
        PenyuluhForm.resize(500, 380)
        self.verticalLayout = QVBoxLayout(PenyuluhForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lblId = QLabel(PenyuluhForm)
        self.lblId.setObjectName(u"lblId")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblId)

        self.id_penyuluh = QSpinBox(PenyuluhForm)
        self.id_penyuluh.setObjectName(u"id_penyuluh")
        self.id_penyuluh.setEnabled(False)
        self.id_penyuluh.setMaximum(2147483647)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.id_penyuluh)

        self.lblNama = QLabel(PenyuluhForm)
        self.lblNama.setObjectName(u"lblNama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblNama)

        self.nama = QLineEdit(PenyuluhForm)
        self.nama.setObjectName(u"nama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.nama)

        self.lblAlamat = QLabel(PenyuluhForm)
        self.lblAlamat.setObjectName(u"lblAlamat")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblAlamat)

        self.alamat = QLineEdit(PenyuluhForm)
        self.alamat.setObjectName(u"alamat")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.alamat)

        self.lblStatus = QLabel(PenyuluhForm)
        self.lblStatus.setObjectName(u"lblStatus")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblStatus)

        self.status = QComboBox(PenyuluhForm)
        self.status.addItem("")
        self.status.addItem("")
        self.status.setObjectName(u"status")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.status)

        self.lblSubsektor = QLabel(PenyuluhForm)
        self.lblSubsektor.setObjectName(u"lblSubsektor")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblSubsektor)

        self.subsektor = QComboBox(PenyuluhForm)
        self.subsektor.addItem("")
        self.subsektor.addItem("")
        self.subsektor.addItem("")
        self.subsektor.addItem("")
        self.subsektor.addItem("")
        self.subsektor.setObjectName(u"subsektor")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.subsektor)

        self.lblMulai = QLabel(PenyuluhForm)
        self.lblMulai.setObjectName(u"lblMulai")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblMulai)

        self.tgl_mulai = QDateEdit(PenyuluhForm)
        self.tgl_mulai.setObjectName(u"tgl_mulai")
        self.tgl_mulai.setCalendarPopup(True)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.tgl_mulai)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnSave = QPushButton(PenyuluhForm)
        self.btnSave.setObjectName(u"btnSave")

        self.buttonLayout.addWidget(self.btnSave)

        self.btnClear = QPushButton(PenyuluhForm)
        self.btnClear.setObjectName(u"btnClear")

        self.buttonLayout.addWidget(self.btnClear)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer)

        self.btnClose = QPushButton(PenyuluhForm)
        self.btnClose.setObjectName(u"btnClose")

        self.buttonLayout.addWidget(self.btnClose)


        self.verticalLayout.addLayout(self.buttonLayout)


        self.retranslateUi(PenyuluhForm)

        QMetaObject.connectSlotsByName(PenyuluhForm)
    # setupUi

    def retranslateUi(self, PenyuluhForm):
        PenyuluhForm.setWindowTitle(QCoreApplication.translate("PenyuluhForm", u"Form Penyuluh (Sederhana)", None))
        self.lblId.setText(QCoreApplication.translate("PenyuluhForm", u"ID Penyuluh", None))
        self.lblNama.setText(QCoreApplication.translate("PenyuluhForm", u"Nama", None))
        self.lblAlamat.setText(QCoreApplication.translate("PenyuluhForm", u"Alamat", None))
        self.lblStatus.setText(QCoreApplication.translate("PenyuluhForm", u"Status", None))
        self.status.setItemText(0, QCoreApplication.translate("PenyuluhForm", u"PNS", None))
        self.status.setItemText(1, QCoreApplication.translate("PenyuluhForm", u"Honorer", None))

        self.lblSubsektor.setText(QCoreApplication.translate("PenyuluhForm", u"Subsektor", None))
        self.subsektor.setItemText(0, QCoreApplication.translate("PenyuluhForm", u"Tanaman Pangan", None))
        self.subsektor.setItemText(1, QCoreApplication.translate("PenyuluhForm", u"Hortikultura", None))
        self.subsektor.setItemText(2, QCoreApplication.translate("PenyuluhForm", u"Perkebunan", None))
        self.subsektor.setItemText(3, QCoreApplication.translate("PenyuluhForm", u"Peternakan", None))
        self.subsektor.setItemText(4, QCoreApplication.translate("PenyuluhForm", u"Perikanan", None))

        self.lblMulai.setText(QCoreApplication.translate("PenyuluhForm", u"Tanggal Mulai", None))
        self.btnSave.setText(QCoreApplication.translate("PenyuluhForm", u"Simpan", None))
        self.btnClear.setText(QCoreApplication.translate("PenyuluhForm", u"Bersihkan", None))
        self.btnClose.setText(QCoreApplication.translate("PenyuluhForm", u"Tutup", None))
    # retranslateUi

