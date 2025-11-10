# UI Sederhana (Qt Creator 17, Python 3.11)

Termasuk:
- main.ui (menu tombol sederhana)
- GapoktanForm.ui
- LokasiForm.ui
- PoktanForm.ui
- PetaniForm.ui
- PenyuluhForm.ui

## Cara pakai cepat (PySide6)
```bash
pip install PySide6
```

```python
# app.py
import sys
from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

def load_ui(path):
    f = QFile(path); f.open(QFile.ReadOnly)
    w = QUiLoader().load(f); f.close()
    return w

app = QApplication(sys.argv)
main = load_ui("main.ui")

# event handler: buka form saat tombol ditekan
def open_form(path):
    dlg = load_ui(path)
    # Jika ingin modal seperti dialog:
    if isinstance(dlg, QDialog):
        dlg.exec()
    else:
        dlg.setWindowModality(0)  # non-modal
        dlg.show()

main.findChild(type(main), "btnGapoktan")  # hanya untuk contoh findChild tipe salah

# cara yang benar: gunakan objectName spesifik
main.btnGapoktan.clicked.connect(lambda: open_form("GapoktanForm.ui"))
main.btnPoktan.clicked.connect(lambda: open_form("PoktanForm.ui"))
main.btnPetani.clicked.connect(lambda: open_form("PetaniForm.ui"))
main.btnPenyuluh.clicked.connect(lambda: open_form("PenyuluhForm.ui"))
main.btnLokasi.clicked.connect(lambda: open_form("LokasiForm.ui"))

main.show()
sys.exit(app.exec())
```

Catatan:
- Field ID memakai `QSpinBox` dalam keadaan disabled supaya tidak diubah manual.
- Field relasi (ID Lokasi, ID Gapoktan, ID Poktan) disederhanakan menjadi `QLineEdit` agar mudah dipakai pemula.
- Tombol `Simpan`, `Bersihkan`, `Tutup` belum punya logic — tinggal ditambahkan di kode Python sesuai kebutuhan.
- Jika ingin menjadikan form sebagai `QDialog`, di Qt Designer ubah `QWidget` → `QDialog` lalu tambahkan `QDialogButtonBox` jika perlu.