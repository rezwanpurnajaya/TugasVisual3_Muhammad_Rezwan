# This Python file uses the following encoding: utf-8
import mysql.connector
from mysql.connector import Error

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors


class crud_pertanian:
    """
    CRUD untuk database: db_2310010299
    Default koneksi mengikuti contoh dosen (root, password kosong, localhost).
    Silakan ubah jika database kamu berbeda.
    """
    def __init__(self,
                 host: str = "localhost",
                 user: str = "root",
                 password: str = "",
                 database: str = "db_2310010299"):
        try:
            self.koneksi = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
        except Error as e:
            raise RuntimeError(f"Gagal konek ke MySQL: {e}")

    # -----------------------
    # Helper
    # -----------------------
    def _exec(self, sql: str, params=None, dictionary: bool = False, fetch: str = "none"):
        cur = self.koneksi.cursor(dictionary=dictionary)
        try:
            cur.execute(sql, params or ())
            if fetch == "all":
                return cur.fetchall()
            if fetch == "one":
                return cur.fetchone()
            self.koneksi.commit()
            return None
        finally:
            cur.close()

    def _cetak_pdf(self, headers, rows, filename: str):
        barisData = [headers] + [list(r) for r in rows]
        pdf = SimpleDocTemplate(filename, pagesize=A4)
        table = Table(barisData)
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ]))
        pdf.build([table])

    # =======================
    # LOKASI
    # =======================
    def tambahLokasi(self, id_lokasi, provinsi, kabupaten, kecamatan, desa):
        self._exec(
            "INSERT INTO lokasi (id_lokasi, provinsi, kabupaten, kecamatan, desa) VALUES (%s,%s,%s,%s,%s)",
            (id_lokasi, provinsi, kabupaten, kecamatan, desa)
        )

    def gantiLokasi(self, id_lokasi, provinsi, kabupaten, kecamatan, desa):
        self._exec(
            "UPDATE lokasi SET provinsi=%s, kabupaten=%s, kecamatan=%s, desa=%s WHERE id_lokasi=%s",
            (provinsi, kabupaten, kecamatan, desa, id_lokasi)
        )

    def kurangLokasi(self, id_lokasi):
        self._exec("DELETE FROM lokasi WHERE id_lokasi=%s", (id_lokasi,))

    def dataLokasi(self):
        return self._exec("SELECT * FROM lokasi ORDER BY id_lokasi ASC", dictionary=True, fetch="all")

    def filterLokasi(self, cari: str):
        like = f"%{cari}%"
        return self._exec(
            "SELECT * FROM lokasi WHERE id_lokasi LIKE %s OR provinsi LIKE %s OR kabupaten LIKE %s OR kecamatan LIKE %s OR desa LIKE %s",
            (like, like, like, like, like),
            dictionary=True,
            fetch="all"
        )

    def listLokasi(self):
        # Untuk combobox (gapoktan)
        return self._exec("SELECT id_lokasi, provinsi, kabupaten, kecamatan, desa FROM lokasi ORDER BY id_lokasi", fetch="all")

    def cetakLokasi(self, provinsi: str | None = None):
        if not provinsi:
            rows = self._exec("SELECT id_lokasi, provinsi, kabupaten, kecamatan, desa FROM lokasi ORDER BY id_lokasi", fetch="all")
            self._cetak_pdf(["ID", "Provinsi", "Kabupaten", "Kecamatan", "Desa"], rows, "Laporan Lokasi.pdf")
        else:
            rows = self._exec(
                "SELECT id_lokasi, provinsi, kabupaten, kecamatan, desa FROM lokasi WHERE provinsi=%s ORDER BY id_lokasi",
                (provinsi,),
                fetch="all"
            )
            self._cetak_pdf(["ID", "Provinsi", "Kabupaten", "Kecamatan", "Desa"], rows, "Laporan Lokasi.pdf")

    # =======================
    # GAPOKTAN
    # =======================
    def tambahGapoktan(self, id_gapoktan, nama_gapoktan, ketua, kontak, id_lokasi):
        self._exec(
            "INSERT INTO gapoktan (id_gapoktan, nama_gapoktan, ketua, kontak, id_lokasi) VALUES (%s,%s,%s,%s,%s)",
            (id_gapoktan, nama_gapoktan, ketua, kontak, id_lokasi or None)
        )

    def gantiGapoktan(self, id_gapoktan, nama_gapoktan, ketua, kontak, id_lokasi):
        self._exec(
            "UPDATE gapoktan SET nama_gapoktan=%s, ketua=%s, kontak=%s, id_lokasi=%s WHERE id_gapoktan=%s",
            (nama_gapoktan, ketua, kontak, id_lokasi or None, id_gapoktan)
        )

    def kurangGapoktan(self, id_gapoktan):
        self._exec("DELETE FROM gapoktan WHERE id_gapoktan=%s", (id_gapoktan,))

    def dataGapoktan(self):
        return self._exec("SELECT * FROM gapoktan ORDER BY id_gapoktan ASC", dictionary=True, fetch="all")

    def filterGapoktan(self, cari: str):
        like = f"%{cari}%"
        return self._exec(
            "SELECT * FROM gapoktan WHERE id_gapoktan LIKE %s OR nama_gapoktan LIKE %s OR ketua LIKE %s OR kontak LIKE %s",
            (like, like, like, like),
            dictionary=True,
            fetch="all"
        )

    def listGapoktan(self):
        # Untuk combobox (poktan)
        return self._exec("SELECT id_gapoktan, nama_gapoktan FROM gapoktan ORDER BY id_gapoktan", fetch="all")

    def cetakGapoktan(self, id_lokasi: str | None = None):
        if not id_lokasi:
            rows = self._exec("SELECT id_gapoktan, nama_gapoktan, ketua, kontak, id_lokasi FROM gapoktan ORDER BY id_gapoktan", fetch="all")
        else:
            rows = self._exec(
                "SELECT id_gapoktan, nama_gapoktan, ketua, kontak, id_lokasi FROM gapoktan WHERE id_lokasi=%s ORDER BY id_gapoktan",
                (id_lokasi,),
                fetch="all"
            )
        self._cetak_pdf(["ID", "Nama Gapoktan", "Ketua", "Kontak", "ID Lokasi"], rows, "Laporan Gapoktan.pdf")

    # =======================
    # POKTAN
    # =======================
    def tambahPoktan(self, id_poktan, nama_poktan, ketua, kelas, id_gapoktan):
        self._exec(
            "INSERT INTO poktan (id_poktan, nama_poktan, ketua, kelas, id_gapoktan) VALUES (%s,%s,%s,%s,%s)",
            (id_poktan, nama_poktan, ketua, kelas, id_gapoktan or None)
        )

    def gantiPoktan(self, id_poktan, nama_poktan, ketua, kelas, id_gapoktan):
        self._exec(
            "UPDATE poktan SET nama_poktan=%s, ketua=%s, kelas=%s, id_gapoktan=%s WHERE id_poktan=%s",
            (nama_poktan, ketua, kelas, id_gapoktan or None, id_poktan)
        )

    def kurangPoktan(self, id_poktan):
        self._exec("DELETE FROM poktan WHERE id_poktan=%s", (id_poktan,))

    def dataPoktan(self):
        return self._exec("SELECT * FROM poktan ORDER BY id_poktan ASC", dictionary=True, fetch="all")

    def filterPoktan(self, cari: str):
        like = f"%{cari}%"
        return self._exec(
            "SELECT * FROM poktan WHERE id_poktan LIKE %s OR nama_poktan LIKE %s OR ketua LIKE %s OR kelas LIKE %s",
            (like, like, like, like),
            dictionary=True,
            fetch="all"
        )

    def listPoktan(self):
        # Untuk combobox (petani)
        return self._exec("SELECT id_poktan, nama_poktan FROM poktan ORDER BY id_poktan", fetch="all")

    def cetakPoktan(self, kelas: str | None = None):
        if not kelas:
            rows = self._exec("SELECT id_poktan, nama_poktan, ketua, kelas, id_gapoktan FROM poktan ORDER BY id_poktan", fetch="all")
        else:
            rows = self._exec(
                "SELECT id_poktan, nama_poktan, ketua, kelas, id_gapoktan FROM poktan WHERE kelas=%s ORDER BY id_poktan",
                (kelas,),
                fetch="all"
            )
        self._cetak_pdf(["ID", "Nama Poktan", "Ketua", "Kelas", "ID Gapoktan"], rows, "Laporan Poktan.pdf")

    # =======================
    # PETANI
    # =======================
    def tambahPetani(self, id_petani, nama, alamat, komoditas, luas_lahan, umur, kontak, id_poktan):
        self._exec(
            "INSERT INTO petani (id_petani, nama, alamat, komoditas, luas_lahan, umur, kontak, id_poktan) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
            (id_petani, nama, alamat, komoditas, luas_lahan, umur, kontak, id_poktan or None)
        )

    def gantiPetani(self, id_petani, nama, alamat, komoditas, luas_lahan, umur, kontak, id_poktan):
        self._exec(
            "UPDATE petani SET nama=%s, alamat=%s, komoditas=%s, luas_lahan=%s, umur=%s, kontak=%s, id_poktan=%s WHERE id_petani=%s",
            (nama, alamat, komoditas, luas_lahan, umur, kontak, id_poktan or None, id_petani)
        )

    def kurangPetani(self, id_petani):
        self._exec("DELETE FROM petani WHERE id_petani=%s", (id_petani,))

    def dataPetani(self):
        return self._exec("SELECT * FROM petani ORDER BY id_petani ASC", dictionary=True, fetch="all")

    def filterPetani(self, cari: str):
        like = f"%{cari}%"
        return self._exec(
            "SELECT * FROM petani WHERE id_petani LIKE %s OR nama LIKE %s OR alamat LIKE %s OR komoditas LIKE %s OR kontak LIKE %s",
            (like, like, like, like, like),
            dictionary=True,
            fetch="all"
        )

    def cetakPetani(self, komoditas: str | None = None):
        if not komoditas:
            rows = self._exec("SELECT id_petani, nama, alamat, komoditas, luas_lahan, umur, kontak, id_poktan FROM petani ORDER BY id_petani", fetch="all")
        else:
            rows = self._exec(
                "SELECT id_petani, nama, alamat, komoditas, luas_lahan, umur, kontak, id_poktan FROM petani WHERE komoditas=%s ORDER BY id_petani",
                (komoditas,),
                fetch="all"
            )
        self._cetak_pdf(["ID", "Nama", "Alamat", "Komoditas", "Luas", "Umur", "Kontak", "ID Poktan"], rows, "Laporan Petani.pdf")

    # =======================
    # PENYULUH
    # =======================
    def tambahPenyuluh(self, id_penyuluh, nama, alamat, status, subsektor, tgl_mulai):
        self._exec(
            "INSERT INTO penyuluh (id_penyuluh, nama, alamat, status, subsektor, tgl_mulai) VALUES (%s,%s,%s,%s,%s,%s)",
            (id_penyuluh, nama, alamat, status, subsektor, tgl_mulai or None)
        )

    def gantiPenyuluh(self, id_penyuluh, nama, alamat, status, subsektor, tgl_mulai):
        self._exec(
            "UPDATE penyuluh SET nama=%s, alamat=%s, status=%s, subsektor=%s, tgl_mulai=%s WHERE id_penyuluh=%s",
            (nama, alamat, status, subsektor, tgl_mulai or None, id_penyuluh)
        )

    def kurangPenyuluh(self, id_penyuluh):
        self._exec("DELETE FROM penyuluh WHERE id_penyuluh=%s", (id_penyuluh,))

    def dataPenyuluh(self):
        return self._exec("SELECT * FROM penyuluh ORDER BY id_penyuluh ASC", dictionary=True, fetch="all")

    def filterPenyuluh(self, cari: str):
        like = f"%{cari}%"
        return self._exec(
            "SELECT * FROM penyuluh WHERE id_penyuluh LIKE %s OR nama LIKE %s OR alamat LIKE %s OR status LIKE %s OR subsektor LIKE %s",
            (like, like, like, like, like),
            dictionary=True,
            fetch="all"
        )

    def cetakPenyuluh(self, status: str | None = None):
        if not status:
            rows = self._exec("SELECT id_penyuluh, nama, alamat, status, subsektor, tgl_mulai FROM penyuluh ORDER BY id_penyuluh", fetch="all")
        else:
            rows = self._exec(
                "SELECT id_penyuluh, nama, alamat, status, subsektor, tgl_mulai FROM penyuluh WHERE status=%s ORDER BY id_penyuluh",
                (status,),
                fetch="all"
            )
        self._cetak_pdf(["ID", "Nama", "Alamat", "Status", "Subsektor", "Tgl Mulai"], rows, "Laporan Penyuluh.pdf")
