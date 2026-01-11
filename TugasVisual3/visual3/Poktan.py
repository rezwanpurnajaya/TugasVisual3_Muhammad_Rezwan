# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QVBoxLayout
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from crud import crud_pertanian


class form_poktan(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya = QFile("poktan.ui")
        filenya.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formpoktan = loader.load(filenya)

        # Tempelkan UI ke window ini agar ukuran mengikuti .ui
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.formpoktan)

        # Ikuti ukuran yang diatur di file .ui (geometry/minimumSize)
        self.setMinimumSize(self.formpoktan.minimumSize())
        self.resize(self.formpoktan.size())

        self.setWindowTitle("Data Poktan")

        self.aksi = crud_pertanian()

        # combo filter
        self.formpoktan.comboFilter.addItem("Kelas")

        self.refresh_gapoktan()

        self.formpoktan.BtnSimpan.clicked.connect(self.simpan)
        self.formpoktan.BtnUbah.clicked.connect(self.ubah)
        self.formpoktan.BtnHapus.clicked.connect(self.hapus)
        self.formpoktan.lineCari.textChanged.connect(self.cari)
        self.formpoktan.btnCetak.clicked.connect(self.cetak)

        self.formpoktan.tblPoktan.itemSelectionChanged.connect(self.isiDariTabel)

        self.tampil()

    def refresh_gapoktan(self):
        self.formpoktan.ComboGapoktan.clear()
        try:
            data = self.aksi.listGapoktan()
            for row in data:
                # row = (id_gapoktan, nama_gapoktan)
                txt = f"{row[0]} - {row[1]}"
                self.formpoktan.ComboGapoktan.addItem(txt, row[0])
        except Exception:
            pass

    def _msg(self, teks: str):
        QMessageBox.information(self, "Informasi", teks)

    def isiDariTabel(self):
        row = self.formpoktan.tblPoktan.currentRow()
        if row < 0:
            return
        tbl = self.formpoktan.tblPoktan
        self.formpoktan.EditId.setText(tbl.item(row, 0).text())
        self.formpoktan.EditNama.setText(tbl.item(row, 1).text())
        self.formpoktan.EditKetua.setText(tbl.item(row, 2).text())
        self.formpoktan.EditKelas.setText(tbl.item(row, 3).text())

        id_gapoktan = tbl.item(row, 4).text()
        idx = self.formpoktan.ComboGapoktan.findData(int(id_gapoktan)) if id_gapoktan.isdigit() else -1
        if idx >= 0:
            self.formpoktan.ComboGapoktan.setCurrentIndex(idx)

    def tampil(self):
        self.formpoktan.tblPoktan.setRowCount(0)
        data = self.aksi.dataPoktan()
        for i, b in enumerate(data):
            self.formpoktan.tblPoktan.insertRow(i)
            self.formpoktan.tblPoktan.setItem(i, 0, QTableWidgetItem(str(b["id_poktan"])))
            self.formpoktan.tblPoktan.setItem(i, 1, QTableWidgetItem(str(b["nama_poktan"])))
            self.formpoktan.tblPoktan.setItem(i, 2, QTableWidgetItem(str(b["ketua"])))
            self.formpoktan.tblPoktan.setItem(i, 3, QTableWidgetItem(str(b["kelas"])))
            self.formpoktan.tblPoktan.setItem(i, 4, QTableWidgetItem(str(b["id_gapoktan"])))

    def cari(self):
        cari = self.formpoktan.lineCari.text()
        self.formpoktan.tblPoktan.setRowCount(0)
        data = self.aksi.filterPoktan(cari)
        for i, b in enumerate(data):
            self.formpoktan.tblPoktan.insertRow(i)
            self.formpoktan.tblPoktan.setItem(i, 0, QTableWidgetItem(str(b["id_poktan"])))
            self.formpoktan.tblPoktan.setItem(i, 1, QTableWidgetItem(str(b["nama_poktan"])))
            self.formpoktan.tblPoktan.setItem(i, 2, QTableWidgetItem(str(b["ketua"])))
            self.formpoktan.tblPoktan.setItem(i, 3, QTableWidgetItem(str(b["kelas"])))
            self.formpoktan.tblPoktan.setItem(i, 4, QTableWidgetItem(str(b["id_gapoktan"])))

    def simpan(self):
        if not self.formpoktan.EditId.text().strip():
            self._msg("ID Poktan belum diisi")
            self.formpoktan.EditId.setFocus()
            return
        if not self.formpoktan.EditNama.text().strip():
            self._msg("Nama Poktan belum diisi")
            self.formpoktan.EditNama.setFocus()
            return

        id_gapoktan = self.formpoktan.ComboGapoktan.currentData()
        self.aksi.tambahPoktan(
            self.formpoktan.EditId.text(),
            self.formpoktan.EditNama.text(),
            self.formpoktan.EditKetua.text(),
            self.formpoktan.EditKelas.text(),
            id_gapoktan
        )
        self.tampil()
        self._msg("Data berhasil disimpan")

    def ubah(self):
        id_gapoktan = self.formpoktan.ComboGapoktan.currentData()
        self.aksi.gantiPoktan(
            self.formpoktan.EditId.text(),
            self.formpoktan.EditNama.text(),
            self.formpoktan.EditKetua.text(),
            self.formpoktan.EditKelas.text(),
            id_gapoktan
        )
        self.tampil()
        self._msg("Data berhasil diubah")

    def hapus(self):
        pesan = QMessageBox.information(self, "Konfirmasi", "Yakin menghapus data ini?",
                                        QMessageBox.Yes | QMessageBox.No)
        if pesan != QMessageBox.Yes:
            return
        self.aksi.kurangPoktan(self.formpoktan.EditId.text())
        self.tampil()
        self._msg("Data berhasil dihapus")

    def cetak(self):
        opt = self.formpoktan.comboFilter.currentText()
        nilai = self.formpoktan.txtFilter.text().strip()
        if opt == "Semua":
            self.aksi.cetakPoktan(None)
        elif opt == "Kelas":
            self.aksi.cetakPoktan(nilai)
        self._msg("PDF tersimpan: Laporan Poktan.pdf")
