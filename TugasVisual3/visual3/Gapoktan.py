# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QVBoxLayout
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from crud import crud_pertanian


class form_gapoktan(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya = QFile("gapoktan.ui")
        filenya.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formgapoktan = loader.load(filenya)

        # Tempelkan UI ke window ini agar ukuran mengikuti .ui
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.formgapoktan)

        # Ikuti ukuran yang diatur di file .ui (geometry/minimumSize)
        self.setMinimumSize(self.formgapoktan.minimumSize())
        self.resize(self.formgapoktan.size())

        self.setWindowTitle("Data Gapoktan")

        self.aksi = crud_pertanian()

        # combo filter (item "Semua" sudah ada)
        self.formgapoktan.comboFilter.addItem("ID Lokasi")

        # isi combobox lokasi
        self.refresh_lokasi()

        self.formgapoktan.BtnSimpan.clicked.connect(self.simpan)
        self.formgapoktan.BtnUbah.clicked.connect(self.ubah)
        self.formgapoktan.BtnHapus.clicked.connect(self.hapus)
        self.formgapoktan.lineCari.textChanged.connect(self.cari)
        self.formgapoktan.btnCetak.clicked.connect(self.cetak)

        self.formgapoktan.tblGapoktan.itemSelectionChanged.connect(self.isiDariTabel)

        self.tampil()

    def refresh_lokasi(self):
        self.formgapoktan.ComboLokasi.clear()
        try:
            data = self.aksi.listLokasi()
            for row in data:
                # row = (id_lokasi, provinsi, kabupaten, kecamatan, desa)
                txt = f"{row[0]} - {row[1]}, {row[2]}, {row[3]}, {row[4]}"
                self.formgapoktan.ComboLokasi.addItem(txt, row[0])
        except Exception:
            pass

    def _msg(self, teks: str):
        QMessageBox.information(self, "Informasi", teks)

    def isiDariTabel(self):
        row = self.formgapoktan.tblGapoktan.currentRow()
        if row < 0:
            return
        tbl = self.formgapoktan.tblGapoktan
        self.formgapoktan.EditId.setText(tbl.item(row, 0).text())
        self.formgapoktan.EditNama.setText(tbl.item(row, 1).text())
        self.formgapoktan.EditKetua.setText(tbl.item(row, 2).text())
        self.formgapoktan.EditKontak.setText(tbl.item(row, 3).text())

        id_lokasi = tbl.item(row, 4).text()
        idx = self.formgapoktan.ComboLokasi.findData(int(id_lokasi)) if id_lokasi.isdigit() else -1
        if idx >= 0:
            self.formgapoktan.ComboLokasi.setCurrentIndex(idx)

    def tampil(self):
        self.formgapoktan.tblGapoktan.setRowCount(0)
        data = self.aksi.dataGapoktan()
        for i, b in enumerate(data):
            self.formgapoktan.tblGapoktan.insertRow(i)
            self.formgapoktan.tblGapoktan.setItem(i, 0, QTableWidgetItem(str(b["id_gapoktan"])))
            self.formgapoktan.tblGapoktan.setItem(i, 1, QTableWidgetItem(str(b["nama_gapoktan"])))
            self.formgapoktan.tblGapoktan.setItem(i, 2, QTableWidgetItem(str(b["ketua"])))
            self.formgapoktan.tblGapoktan.setItem(i, 3, QTableWidgetItem(str(b["kontak"])))
            self.formgapoktan.tblGapoktan.setItem(i, 4, QTableWidgetItem(str(b["id_lokasi"])))

    def cari(self):
        cari = self.formgapoktan.lineCari.text()
        self.formgapoktan.tblGapoktan.setRowCount(0)
        data = self.aksi.filterGapoktan(cari)
        for i, b in enumerate(data):
            self.formgapoktan.tblGapoktan.insertRow(i)
            self.formgapoktan.tblGapoktan.setItem(i, 0, QTableWidgetItem(str(b["id_gapoktan"])))
            self.formgapoktan.tblGapoktan.setItem(i, 1, QTableWidgetItem(str(b["nama_gapoktan"])))
            self.formgapoktan.tblGapoktan.setItem(i, 2, QTableWidgetItem(str(b["ketua"])))
            self.formgapoktan.tblGapoktan.setItem(i, 3, QTableWidgetItem(str(b["kontak"])))
            self.formgapoktan.tblGapoktan.setItem(i, 4, QTableWidgetItem(str(b["id_lokasi"])))

    def simpan(self):
        if not self.formgapoktan.EditId.text().strip():
            self._msg("ID Gapoktan belum diisi")
            self.formgapoktan.EditId.setFocus()
            return
        if not self.formgapoktan.EditNama.text().strip():
            self._msg("Nama Gapoktan belum diisi")
            self.formgapoktan.EditNama.setFocus()
            return

        id_lokasi = self.formgapoktan.ComboLokasi.currentData()
        self.aksi.tambahGapoktan(
            self.formgapoktan.EditId.text(),
            self.formgapoktan.EditNama.text(),
            self.formgapoktan.EditKetua.text(),
            self.formgapoktan.EditKontak.text(),
            id_lokasi
        )
        self.tampil()
        self._msg("Data berhasil disimpan")

    def ubah(self):
        id_lokasi = self.formgapoktan.ComboLokasi.currentData()
        self.aksi.gantiGapoktan(
            self.formgapoktan.EditId.text(),
            self.formgapoktan.EditNama.text(),
            self.formgapoktan.EditKetua.text(),
            self.formgapoktan.EditKontak.text(),
            id_lokasi
        )
        self.tampil()
        self._msg("Data berhasil diubah")

    def hapus(self):
        pesan = QMessageBox.information(self, "Konfirmasi", "Yakin menghapus data ini?",
                                        QMessageBox.Yes | QMessageBox.No)
        if pesan != QMessageBox.Yes:
            return
        self.aksi.kurangGapoktan(self.formgapoktan.EditId.text())
        self.tampil()
        self._msg("Data berhasil dihapus")

    def cetak(self):
        opt = self.formgapoktan.comboFilter.currentText()
        nilai = self.formgapoktan.txtFilter.text().strip()
        if opt == "Semua":
            self.aksi.cetakGapoktan(None)
        elif opt == "ID Lokasi":
            self.aksi.cetakGapoktan(nilai)
        self._msg("PDF tersimpan: Laporan Gapoktan.pdf")
