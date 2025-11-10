from PySide6.QtWidgets import QWidget, QMessageBox, QLineEdit, QSpinBox, QDoubleSpinBox, QComboBox, QDateEdit
from PySide6.QtCore import QFile, QDate
from PySide6.QtUiTools import QUiLoader
import crud

def _load_ui(p):
    f = QFile(p); f.open(QFile.ReadOnly)
    try: return QUiLoader().load(f)
    finally: f.close()

def _iter_controls(root):
    lst = []
    lst += root.findChildren(QLineEdit)
    lst += root.findChildren(QSpinBox)
    lst += root.findChildren(QDoubleSpinBox)
    lst += root.findChildren(QComboBox)
    lst += root.findChildren(QDateEdit)
    return lst

def _collect(root):
    data = {}
    for w in _iter_controls(root):
        name = w.objectName() or ""
        if not name or name.startswith("qt_"):
            continue

        if isinstance(w, QSpinBox):
            val = int(w.value())
        elif isinstance(w, QDoubleSpinBox):
            val = float(w.value())
        elif isinstance(w, QComboBox):
            val = w.currentData()
            if val in (None, ""):
                val = w.currentText()
        elif isinstance(w, QDateEdit):
            val = w.date().toString("yyyy-MM-dd")
        else:
            val = w.text()

        data[name] = val
    return data

def _clear(root):
    for w in _iter_controls(root):
        if isinstance(w, QLineEdit): w.clear()
        elif isinstance(w, QSpinBox): w.setValue(0)
        elif isinstance(w, QDoubleSpinBox): w.setValue(0.0)
        elif isinstance(w, QComboBox): w.setCurrentIndex(0)
        elif isinstance(w, QDateEdit): w.setDate(QDate.currentDate())

class PenyuluhForm(QWidget):
    PK = "id_penyuluh"
    def __init__(self, parent=None):
        super().__init__(parent)
        self.w = _load_ui("PenyuluhForm.ui"); self.w.setParent(self)
        self.w.setWindowTitle("Penyuluh (Sederhana)")
        self.w.btnSave.clicked.connect(self.on_save)
        self.w.btnClear.clicked.connect(self.on_clear)
        self.w.btnClose.clicked.connect(self.close)

    def on_clear(self):
        _clear(self.w); QMessageBox.information(self, "Info", "Form dibersihkan.")

    def on_save(self):
        data = _collect(self.w)
        pk = int(data.get(self.PK) or 0) if str(data.get(self.PK) or "").strip() else 0
        try:
            if not pk:
                new_id = crud.penyuluh_insert(data)
                wpk = getattr(self.w, self.PK, None)
                if wpk is not None:
                    if hasattr(wpk, "setValue"): wpk.setValue(int(new_id))
                    elif hasattr(wpk, "setText"): wpk.setText(str(new_id))
                QMessageBox.information(self, "Info", f"Data ditambahkan (ID: {new_id})")
            else:
                data.pop(self.PK, None)
                rows = crud.penyuluh_update(pk, data)
                QMessageBox.information(self, "Info", f"Perubahan disimpan ({rows} baris).")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def show(self): self.w.show()
