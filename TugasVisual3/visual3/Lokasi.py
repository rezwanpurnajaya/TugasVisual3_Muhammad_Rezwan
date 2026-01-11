# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QVBoxLayout
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from crud import crud_pertanian


class form_lokasi(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya = QFile("lokasi.ui")
        filenya.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formlokasi = loader.load(filenya)

        # Tempelkan UI ke window ini agar ukuran mengikuti .ui
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.formlokasi)

        # Ikuti ukuran yang diatur di file .ui (geometry/minimumSize)
        self.setMinimumSize(self.formlokasi.minimumSize())
        self.resize(self.formlokasi.size())

        self.setWindowTitle("Data Lokasi")

        self.aksi = crud_pertanian()

        # combo filter (item "Semua" sudah ada dari .ui)
        self.formlokasi.comboFilter.addItem("Provinsi")

        self.formlokasi.BtnSimpan.clicked.connect(self.simpan)
        self.formlokasi.BtnUbah.clicked.connect(self.ubah)
        self.formlokasi.BtnHapus.clicked.connect(self.hapus)
        self.formlokasi.lineCari.textChanged.connect(self.cari)
        self.formlokasi.btnCetak.clicked.connect(self.cetak)

        self.formlokasi.tblLokasi.itemSelectionChanged.connect(self.isiDariTabel)

        self.tampil()

    def _msg(self, teks: str):
        QMessageBox.information(self, "Informasi", teks)

    def isiDariTabel(self):
        row = self.formlokasi.tblLokasi.currentRow()
        if row < 0:
            return
        tbl = self.formlokasi.tblLokasi
        self.formlokasi.EditId.setText(tbl.item(row, 0).text())
        self.formlokasi.EditProvinsi.setText(tbl.item(row, 1).text())
        self.formlokasi.EditKabupaten.setText(tbl.item(row, 2).text())
        self.formlokasi.EditKecamatan.setText(tbl.item(row, 3).text())
        self.formlokasi.EditDesa.setText(tbl.item(row, 4).text())

    def tampil(self):
        self.formlokasi.tblLokasi.setRowCount(0)
        data = self.aksi.dataLokasi()
        for i, b in enumerate(data):
            self.formlokasi.tblLokasi.insertRow(i)
            self.formlokasi.tblLokasi.setItem(i, 0, QTableWidgetItem(str(b["id_lokasi"])))
            self.formlokasi.tblLokasi.setItem(i, 1, QTableWidgetItem(str(b["provinsi"])))
            self.formlokasi.tblLokasi.setItem(i, 2, QTableWidgetItem(str(b["kabupaten"])))
            self.formlokasi.tblLokasi.setItem(i, 3, QTableWidgetItem(str(b["kecamatan"])))
            self.formlokasi.tblLokasi.setItem(i, 4, QTableWidgetItem(str(b["desa"])))

    def cari(self):
        cari = self.formlokasi.lineCari.text()
        self.formlokasi.tblLokasi.setRowCount(0)
        data = self.aksi.filterLokasi(cari)
        for i, b in enumerate(data):
            self.formlokasi.tblLokasi.insertRow(i)
            self.formlokasi.tblLokasi.setItem(i, 0, QTableWidgetItem(str(b["id_lokasi"])))
            self.formlokasi.tblLokasi.setItem(i, 1, QTableWidgetItem(str(b["provinsi"])))
            self.formlokasi.tblLokasi.setItem(i, 2, QTableWidgetItem(str(b["kabupaten"])))
            self.formlokasi.tblLokasi.setItem(i, 3, QTableWidgetItem(str(b["kecamatan"])))
            self.formlokasi.tblLokasi.setItem(i, 4, QTableWidgetItem(str(b["desa"])))

    def simpan(self):
        if not self.formlokasi.EditId.text().strip():
            self._msg("ID Lokasi belum diisi")
            self.formlokasi.EditId.setFocus()
            return
        if not self.formlokasi.EditProvinsi.text().strip():
            self._msg("Provinsi belum diisi")
            self.formlokasi.EditProvinsi.setFocus()
            return

        self.aksi.tambahLokasi(
            self.formlokasi.EditId.text(),
            self.formlokasi.EditProvinsi.text(),
            self.formlokasi.EditKabupaten.text(),
            self.formlokasi.EditKecamatan.text(),
            self.formlokasi.EditDesa.text(),
        )
        self.tampil()
        self._msg("Data berhasil disimpan")

    def ubah(self):
        self.aksi.gantiLokasi(
            self.formlokasi.EditId.text(),
            self.formlokasi.EditProvinsi.text(),
            self.formlokasi.EditKabupaten.text(),
            self.formlokasi.EditKecamatan.text(),
            self.formlokasi.EditDesa.text(),
        )
        self.tampil()
        self._msg("Data berhasil diubah")

    def hapus(self):
        pesan = QMessageBox.information(self, "Konfirmasi", "Yakin menghapus data ini?",
                                        QMessageBox.Yes | QMessageBox.No)
        if pesan != QMessageBox.Yes:
            return
        self.aksi.kurangLokasi(self.formlokasi.EditId.text())
        self.tampil()
        self._msg("Data berhasil dihapus")

    def cetak(self):
        opt = self.formlokasi.comboFilter.currentText()
        nilai = self.formlokasi.txtFilter.text().strip()
        if opt == "Semua":
            self.aksi.cetakLokasi(None)
        elif opt == "Provinsi":
            self.aksi.cetakLokasi(nilai)
        self._msg("PDF tersimpan: Laporan Lokasi.pdf")
