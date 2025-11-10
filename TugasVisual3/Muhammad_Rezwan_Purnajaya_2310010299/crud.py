# crud.py — mysql.connector + helper CRUD (autocommit + cek FK)
from typing import Dict, Any, List, Tuple
import os
import mysql.connector
from mysql.connector import errors

# ==== KONFIG DB ====
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "")
DB_NAME = os.getenv("DB_NAME", "db_2310010299")  # GANTI sesuai DB kamu

class crud:
    def __init__(self):
        try:
            self.koneksi = mysql.connector.connect(
                host=DB_HOST, port=DB_PORT,
                user=DB_USER, password=DB_PASS,
                database=DB_NAME, autocommit=True,
            )
        except errors.ProgrammingError as e:
            if e.errno == 1049:
                raise RuntimeError(
                    f"Database '{DB_NAME}' belum ada. Ganti DB_NAME di crud.py atau buat databasenya."
                ) from e
            raise

    # ---------- util ----------
    def _cursor(self, dict_cursor: bool = False):
        if not self.koneksi.is_connected():
            self.koneksi.reconnect()
        return self.koneksi.cursor(dictionary=dict_cursor)

    def _exec(self, sql: str, params: Tuple[Any, ...] = ()):
        cur = self._cursor()
        try:
            cur.execute(sql, params)
            return cur
        finally:
            cur.close()

    def _fetchall(self, sql: str, params: Tuple[Any, ...] = (), dicts=True):
        cur = self._cursor(dict_cursor=dicts)
        try:
            cur.execute(sql, params)
            return cur.fetchall()
        finally:
            cur.close()

    def _fetchone(self, sql: str, params: Tuple[Any, ...] = (), dicts=True):
        cur = self._cursor(dict_cursor=dicts)
        try:
            cur.execute(sql, params)
            return cur.fetchone()
        finally:
            cur.close()

    def insert(self, table: str, pk_col: str, data: Dict[str, Any]) -> int:
        items = [(k, v) for k, v in data.items() if k != pk_col and v is not None]
        if not items:
            raise ValueError("Tidak ada data untuk disimpan.")
        cols = [k for k, _ in items]
        vals = [v for _, v in items]
        placeholders = ", ".join(["%s"] * len(cols))
        colnames = ", ".join(cols)
        sql = f"INSERT INTO {table} ({colnames}) VALUES ({placeholders})"
        cur = self._cursor()
        try:
            cur.execute(sql, tuple(vals))
            return cur.lastrowid or int(data.get(pk_col, 0) or 0)
        finally:
            cur.close()


    def update(self, table: str, pk_col: str, pk_val: Any, data: Dict[str, Any]) -> int:
        sets = [f"{k}=%s" for k in data.keys() if k != pk_col]
        vals = [data[k] for k in data.keys() if k != pk_col]
        if not sets:
            return 0
        sql = f"UPDATE {table} SET {', '.join(sets)} WHERE {pk_col}=%s"
        vals.append(pk_val)
        cur = self._cursor()
        try:
            cur.execute(sql, tuple(vals))
            return cur.rowcount
        finally:
            cur.close()

    # ---------- exists helpers (buat cek FK) ----------
    def exists(self, table: str, id_col: str, val: Any) -> bool:
        row = self._fetchone(f"SELECT 1 FROM {table} WHERE {id_col}=%s LIMIT 1", (val,))
        return bool(row)

    def lokasi_exists(self, id_lokasi: Any) -> bool:
        return self.exists("lokasi", "id_lokasi", id_lokasi)

    def gapoktan_exists(self, id_gapoktan: Any) -> bool:
        return self.exists("gapoktan", "id_gapoktan", id_gapoktan)

    def poktan_exists(self, id_poktan: Any) -> bool:
        return self.exists("poktan", "id_poktan", id_poktan)

    # ---------- list (untuk ComboBox opsional) ----------
    def lokasi_list(self) -> List[Dict[str, Any]]:
        return self._fetchall("SELECT id_lokasi, COALESCE(nama_lokasi, nama) AS nama FROM lokasi ORDER BY id_lokasi")

    def gapoktan_list(self) -> List[Dict[str, Any]]:
        return self._fetchall("SELECT id_gapoktan, COALESCE(nama,'') AS nama FROM gapoktan ORDER BY id_gapoktan")

    def poktan_list(self) -> List[Dict[str, Any]]:
        return self._fetchall("SELECT id_poktan, COALESCE(nama,'') AS nama FROM poktan ORDER BY id_poktan")

# ====== SINGLETON DB ======
DB = crud()

# ====== WRAPPERS PER TABEL ======
def gapoktan_insert(data: Dict[str, Any]) -> int:
    # Cek FK id_lokasi kalau ada
    if "id_lokasi" in data and str(data["id_lokasi"]).strip():
        if not DB.lokasi_exists(data["id_lokasi"]):
            raise ValueError(f"id_lokasi {data['id_lokasi']} tidak ditemukan di tabel lokasi.")
    return DB.insert("gapoktan", "id_gapoktan", data)

def gapoktan_update(pk: Any, data: Dict[str, Any]) -> int:
    if "id_lokasi" in data and str(data["id_lokasi"]).strip():
        if not DB.lokasi_exists(data["id_lokasi"]):
            raise ValueError(f"id_lokasi {data['id_lokasi']} tidak ditemukan di tabel lokasi.")
    return DB.update("gapoktan", "id_gapoktan", pk, data)

def poktan_insert(data: Dict[str, Any]) -> int:
    if "id_gapoktan" in data and str(data["id_gapoktan"]).strip():
        if not DB.gapoktan_exists(data["id_gapoktan"]):
            raise ValueError(f"id_gapoktan {data['id_gapoktan']} tidak ditemukan di tabel gapoktan.")
    return DB.insert("poktan", "id_poktan", data)

def poktan_update(pk: Any, data: Dict[str, Any]) -> int:
    if "id_gapoktan" in data and str(data["id_gapoktan"]).strip():
        if not DB.gapoktan_exists(data["id_gapoktan"]):
            raise ValueError(f"id_gapoktan {data['id_gapoktan']} tidak ditemukan di tabel gapoktan.")
    return DB.update("poktan", "id_poktan", pk, data)

def petani_insert(data: Dict[str, Any]) -> int:
    if "id_poktan" in data and str(data["id_poktan"]).strip():
        if not DB.poktan_exists(data["id_poktan"]):
            raise ValueError(f"id_poktan {data['id_poktan']} tidak ditemukan di tabel poktan.")
    return DB.insert("petani", "id_petani", data)

def petani_update(pk: Any, data: Dict[str, Any]) -> int:
    if "id_poktan" in data and str(data["id_poktan"]).strip():
        if not DB.poktan_exists(data["id_poktan"]):
            raise ValueError(f"id_poktan {data['id_poktan']} tidak ditemukan di tabel poktan.")
    return DB.update("petani", "id_petani", pk, data)

def penyuluh_insert(data: Dict[str, Any]) -> int:
    return DB.insert("penyuluh", "id_penyuluh", data)

def penyuluh_update(pk: Any, data: Dict[str, Any]) -> int:
    return DB.update("penyuluh", "id_penyuluh", pk, data)

def lokasi_insert(data: Dict[str, Any]) -> int:
    return DB.insert("lokasi", "id_lokasi", data)

def lokasi_update(pk: Any, data: Dict[str, Any]) -> int:
    return DB.update("lokasi", "id_lokasi", pk, data)
