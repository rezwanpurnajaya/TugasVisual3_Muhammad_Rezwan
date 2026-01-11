# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QVBoxLayout
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from crud import crud_pertanian


class form_petani(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya = QFile("petani.ui")
        filenya.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formpetani = loader.load(filenya)

        # Tempelkan UI ke window ini agar ukuran mengikuti .ui
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.formpetani)

        # Ikuti ukuran yang diatur di file .ui (geometry/minimumSize)
        self.setMinimumSize(self.formpetani.minimumSize())
        self.resize(self.formpetani.size())

        self.setWindowTitle("Data Petani")

        self.aksi = crud_pertanian()

        # combo filter
        self.formpetani.comboFilter.addItem("Komoditas")

        self.refresh_poktan()

        self.formpetani.BtnSimpan.clicked.connect(self.simpan)
        self.formpetani.BtnUbah.clicked.connect(self.ubah)
        self.formpetani.BtnHapus.clicked.connect(self.hapus)
        self.formpetani.lineCari.textChanged.connect(self.cari)
        self.formpetani.btnCetak.clicked.connect(self.cetak)

        self.formpetani.tblPetani.itemSelectionChanged.connect(self.isiDariTabel)

        self.tampil()

    def refresh_poktan(self):
        self.formpetani.ComboPoktan.clear()
        try:
            data = self.aksi.listPoktan()
            for row in data:
                txt = f"{row[0]} - {row[1]}"
                self.formpetani.ComboPoktan.addItem(txt, row[0])
        except Exception:
            pass

    def _msg(self, teks: str):
        QMessageBox.information(self, "Informasi", teks)

    def isiDariTabel(self):
        row = self.formpetani.tblPetani.currentRow()
        if row < 0:
            return
        tbl = self.formpetani.tblPetani
        self.formpetani.EditId.setText(tbl.item(row, 0).text())
        self.formpetani.EditNama.setText(tbl.item(row, 1).text())
        self.formpetani.EditAlamat.setText(tbl.item(row, 2).text())
        self.formpetani.EditKomoditas.setText(tbl.item(row, 3).text())
        try:
            self.formpetani.SpinLuasLahan.setValue(float(tbl.item(row, 4).text()))
        except Exception:
            self.formpetani.SpinLuasLahan.setValue(0.0)
        try:
            self.formpetani.SpinUmur.setValue(int(tbl.item(row, 5).text()))
        except Exception:
            self.formpetani.SpinUmur.setValue(0)
        self.formpetani.EditKontak.setText(tbl.item(row, 6).text())

        id_poktan = tbl.item(row, 7).text()
        idx = self.formpetani.ComboPoktan.findData(int(id_poktan)) if id_poktan.isdigit() else -1
        if idx >= 0:
            self.formpetani.ComboPoktan.setCurrentIndex(idx)

    def tampil(self):
        self.formpetani.tblPetani.setRowCount(0)
        data = self.aksi.dataPetani()
        for i, b in enumerate(data):
            self.formpetani.tblPetani.insertRow(i)
            self.formpetani.tblPetani.setItem(i, 0, QTableWidgetItem(str(b["id_petani"])))
            self.formpetani.tblPetani.setItem(i, 1, QTableWidgetItem(str(b["nama"])))
            self.formpetani.tblPetani.setItem(i, 2, QTableWidgetItem(str(b["alamat"])))
            self.formpetani.tblPetani.setItem(i, 3, QTableWidgetItem(str(b["komoditas"])))
            self.formpetani.tblPetani.setItem(i, 4, QTableWidgetItem(str(b["luas_lahan"])))
            self.formpetani.tblPetani.setItem(i, 5, QTableWidgetItem(str(b["umur"])))
            self.formpetani.tblPetani.setItem(i, 6, QTableWidgetItem(str(b["kontak"])))
            self.formpetani.tblPetani.setItem(i, 7, QTableWidgetItem(str(b["id_poktan"])))

    def cari(self):
        cari = self.formpetani.lineCari.text()
        self.formpetani.tblPetani.setRowCount(0)
        data = self.aksi.filterPetani(cari)
        for i, b in enumerate(data):
            self.formpetani.tblPetani.insertRow(i)
            self.formpetani.tblPetani.setItem(i, 0, QTableWidgetItem(str(b["id_petani"])))
            self.formpetani.tblPetani.setItem(i, 1, QTableWidgetItem(str(b["nama"])))
            self.formpetani.tblPetani.setItem(i, 2, QTableWidgetItem(str(b["alamat"])))
            self.formpetani.tblPetani.setItem(i, 3, QTableWidgetItem(str(b["komoditas"])))
            self.formpetani.tblPetani.setItem(i, 4, QTableWidgetItem(str(b["luas_lahan"])))
            self.formpetani.tblPetani.setItem(i, 5, QTableWidgetItem(str(b["umur"])))
            self.formpetani.tblPetani.setItem(i, 6, QTableWidgetItem(str(b["kontak"])))
            self.formpetani.tblPetani.setItem(i, 7, QTableWidgetItem(str(b["id_poktan"])))

    def simpan(self):
        if not self.formpetani.EditId.text().strip():
            self._msg("ID Petani belum diisi")
            self.formpetani.EditId.setFocus()
            return
        if not self.formpetani.EditNama.text().strip():
            self._msg("Nama belum diisi")
            self.formpetani.EditNama.setFocus()
            return

        id_poktan = self.formpetani.ComboPoktan.currentData()
        self.aksi.tambahPetani(
            self.formpetani.EditId.text(),
            self.formpetani.EditNama.text(),
            self.formpetani.EditAlamat.text(),
            self.formpetani.EditKomoditas.text(),
            float(self.formpetani.SpinLuasLahan.value()),
            int(self.formpetani.SpinUmur.value()),
            self.formpetani.EditKontak.text(),
            id_poktan
        )
        self.tampil()
        self._msg("Data berhasil disimpan")

    def ubah(self):
        id_poktan = self.formpetani.ComboPoktan.currentData()
        self.aksi.gantiPetani(
            self.formpetani.EditId.text(),
            self.formpetani.EditNama.text(),
            self.formpetani.EditAlamat.text(),
            self.formpetani.EditKomoditas.text(),
            float(self.formpetani.SpinLuasLahan.value()),
            int(self.formpetani.SpinUmur.value()),
            self.formpetani.EditKontak.text(),
            id_poktan
        )
        self.tampil()
        self._msg("Data berhasil diubah")

    def hapus(self):
        pesan = QMessageBox.information(self, "Konfirmasi", "Yakin menghapus data ini?",
                                        QMessageBox.Yes | QMessageBox.No)
        if pesan != QMessageBox.Yes:
            return
        self.aksi.kurangPetani(self.formpetani.EditId.text())
        self.tampil()
        self._msg("Data berhasil dihapus")

    def cetak(self):
        opt = self.formpetani.comboFilter.currentText()
        nilai = self.formpetani.txtFilter.text().strip()
        if opt == "Semua":
            self.aksi.cetakPetani(None)
        elif opt == "Komoditas":
            self.aksi.cetakPetani(nilai)
        self._msg("PDF tersimpan: Laporan Petani.pdf")
