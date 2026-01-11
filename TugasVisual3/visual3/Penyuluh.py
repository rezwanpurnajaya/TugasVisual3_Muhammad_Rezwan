# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QVBoxLayout
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from crud import crud_pertanian


class form_penyuluh(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya = QFile("penyuluh.ui")
        filenya.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formpenyuluh = loader.load(filenya)

        # Tempelkan UI ke window ini agar ukuran mengikuti .ui
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.formpenyuluh)

        # Ikuti ukuran yang diatur di file .ui (geometry/minimumSize)
        self.setMinimumSize(self.formpenyuluh.minimumSize())
        self.resize(self.formpenyuluh.size())

        self.setWindowTitle("Data Penyuluh")

        self.aksi = crud_pertanian()

        # combo filter
        self.formpenyuluh.comboFilter.addItem("Status")

        self.formpenyuluh.BtnSimpan.clicked.connect(self.simpan)
        self.formpenyuluh.BtnUbah.clicked.connect(self.ubah)
        self.formpenyuluh.BtnHapus.clicked.connect(self.hapus)
        self.formpenyuluh.lineCari.textChanged.connect(self.cari)
        self.formpenyuluh.btnCetak.clicked.connect(self.cetak)

        self.formpenyuluh.tblPenyuluh.itemSelectionChanged.connect(self.isiDariTabel)

        self.tampil()

    def _msg(self, teks: str):
        QMessageBox.information(self, "Informasi", teks)

    def isiDariTabel(self):
        row = self.formpenyuluh.tblPenyuluh.currentRow()
        if row < 0:
            return
        tbl = self.formpenyuluh.tblPenyuluh
        self.formpenyuluh.EditId.setText(tbl.item(row, 0).text())
        self.formpenyuluh.EditNama.setText(tbl.item(row, 1).text())
        self.formpenyuluh.EditAlamat.setText(tbl.item(row, 2).text())

        status = tbl.item(row, 3).text()
        idx = self.formpenyuluh.ComboStatus.findText(status)
        if idx >= 0:
            self.formpenyuluh.ComboStatus.setCurrentIndex(idx)

        self.formpenyuluh.EditSubsektor.setText(tbl.item(row, 4).text())
        self.formpenyuluh.EditTglMulai.setText(tbl.item(row, 5).text())

    def tampil(self):
        self.formpenyuluh.tblPenyuluh.setRowCount(0)
        data = self.aksi.dataPenyuluh()
        for i, b in enumerate(data):
            self.formpenyuluh.tblPenyuluh.insertRow(i)
            self.formpenyuluh.tblPenyuluh.setItem(i, 0, QTableWidgetItem(str(b["id_penyuluh"])))
            self.formpenyuluh.tblPenyuluh.setItem(i, 1, QTableWidgetItem(str(b["nama"])))
            self.formpenyuluh.tblPenyuluh.setItem(i, 2, QTableWidgetItem(str(b["alamat"])))
            self.formpenyuluh.tblPenyuluh.setItem(i, 3, QTableWidgetItem(str(b["status"])))
            self.formpenyuluh.tblPenyuluh.setItem(i, 4, QTableWidgetItem(str(b["subsektor"])))
            self.formpenyuluh.tblPenyuluh.setItem(i, 5, QTableWidgetItem(str(b["tgl_mulai"])))

    def cari(self):
        cari = self.formpenyuluh.lineCari.text()
        self.formpenyuluh.tblPenyuluh.setRowCount(0)
        data = self.aksi.filterPenyuluh(cari)
        for i, b in enumerate(data):
            self.formpenyuluh.tblPenyuluh.insertRow(i)
            self.formpenyuluh.tblPenyuluh.setItem(i, 0, QTableWidgetItem(str(b["id_penyuluh"])))
            self.formpenyuluh.tblPenyuluh.setItem(i, 1, QTableWidgetItem(str(b["nama"])))
            self.formpenyuluh.tblPenyuluh.setItem(i, 2, QTableWidgetItem(str(b["alamat"])))
            self.formpenyuluh.tblPenyuluh.setItem(i, 3, QTableWidgetItem(str(b["status"])))
            self.formpenyuluh.tblPenyuluh.setItem(i, 4, QTableWidgetItem(str(b["subsektor"])))
            self.formpenyuluh.tblPenyuluh.setItem(i, 5, QTableWidgetItem(str(b["tgl_mulai"])))

    def simpan(self):
        if not self.formpenyuluh.EditId.text().strip():
            self._msg("ID Penyuluh belum diisi")
            self.formpenyuluh.EditId.setFocus()
            return
        if not self.formpenyuluh.EditNama.text().strip():
            self._msg("Nama belum diisi")
            self.formpenyuluh.EditNama.setFocus()
            return

        self.aksi.tambahPenyuluh(
            self.formpenyuluh.EditId.text(),
            self.formpenyuluh.EditNama.text(),
            self.formpenyuluh.EditAlamat.text(),
            self.formpenyuluh.ComboStatus.currentText(),
            self.formpenyuluh.EditSubsektor.text(),
            self.formpenyuluh.EditTglMulai.text().strip()
        )
        self.tampil()
        self._msg("Data berhasil disimpan")

    def ubah(self):
        self.aksi.gantiPenyuluh(
            self.formpenyuluh.EditId.text(),
            self.formpenyuluh.EditNama.text(),
            self.formpenyuluh.EditAlamat.text(),
            self.formpenyuluh.ComboStatus.currentText(),
            self.formpenyuluh.EditSubsektor.text(),
            self.formpenyuluh.EditTglMulai.text().strip()
        )
        self.tampil()
        self._msg("Data berhasil diubah")

    def hapus(self):
        pesan = QMessageBox.information(self, "Konfirmasi", "Yakin menghapus data ini?",
                                        QMessageBox.Yes | QMessageBox.No)
        if pesan != QMessageBox.Yes:
            return
        self.aksi.kurangPenyuluh(self.formpenyuluh.EditId.text())
        self.tampil()
        self._msg("Data berhasil dihapus")

    def cetak(self):
        opt = self.formpenyuluh.comboFilter.currentText()
        nilai = self.formpenyuluh.txtFilter.text().strip()
        if opt == "Semua":
            self.aksi.cetakPenyuluh(None)
        elif opt == "Status":
            self.aksi.cetakPenyuluh(nilai)
        self._msg("PDF tersimpan: Laporan Penyuluh.pdf")
