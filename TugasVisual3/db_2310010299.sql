-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 10 Nov 2025 pada 07.10
-- Versi server: 10.4.28-MariaDB
-- Versi PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_2310010299`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `gapoktan`
--

CREATE TABLE `gapoktan` (
  `id_gapoktan` int(11) NOT NULL,
  `nama_gapoktan` varchar(150) NOT NULL,
  `ketua` varchar(100) DEFAULT NULL,
  `kontak` varchar(50) DEFAULT NULL,
  `id_lokasi` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `gapoktan`
--

INSERT INTO `gapoktan` (`id_gapoktan`, `nama_gapoktan`, `ketua`, `kontak`, `id_lokasi`) VALUES
(1, 'Gapoktan Makmur Bersama', 'Slamet Riyadi', '08123456789', 1),
(2, 'Gapoktan Tani Jaya', 'Sujatmiko', '08123334444', 2);

-- --------------------------------------------------------

--
-- Struktur dari tabel `lokasi`
--

CREATE TABLE `lokasi` (
  `id_lokasi` int(11) NOT NULL,
  `provinsi` varchar(100) NOT NULL,
  `kabupaten` varchar(100) NOT NULL,
  `kecamatan` varchar(100) NOT NULL,
  `desa` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `lokasi`
--

INSERT INTO `lokasi` (`id_lokasi`, `provinsi`, `kabupaten`, `kecamatan`, `desa`) VALUES
(1, 'Jawa Timur', 'Malang', 'Kepanjen', 'Sumberpucung'),
(2, 'Jawa Tengah', 'Magelang', 'Secang', 'Candimulyo');

-- --------------------------------------------------------

--
-- Struktur dari tabel `penyuluh`
--

CREATE TABLE `penyuluh` (
  `id_penyuluh` int(11) NOT NULL,
  `nama` varchar(150) NOT NULL,
  `alamat` varchar(200) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `subsektor` varchar(100) DEFAULT NULL,
  `tgl_mulai` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `penyuluh`
--

INSERT INTO `penyuluh` (`id_penyuluh`, `nama`, `alamat`, `status`, `subsektor`, `tgl_mulai`) VALUES
(1, 'Ratna Dewi', 'Malang', 'PNS', 'Tanaman Pangan', '2019-01-10'),
(2, 'Yudi Pratama', 'Magelang', 'Honorer', 'Hortikultura', '2021-05-15');

-- --------------------------------------------------------

--
-- Struktur dari tabel `petani`
--

CREATE TABLE `petani` (
  `id_petani` int(11) NOT NULL,
  `nama` varchar(150) NOT NULL,
  `alamat` varchar(200) DEFAULT NULL,
  `komoditas` varchar(100) DEFAULT NULL,
  `luas_lahan` decimal(10,2) DEFAULT NULL,
  `umur` int(11) DEFAULT NULL,
  `kontak` varchar(50) DEFAULT NULL,
  `id_poktan` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `petani`
--

INSERT INTO `petani` (`id_petani`, `nama`, `alamat`, `komoditas`, `luas_lahan`, `umur`, `kontak`, `id_poktan`) VALUES
(1, 'Andi Saputra', 'Jl. Raya Sumberpucung', 'Padi', 1.50, 35, '08122334455', 1),
(2, 'Joko Mulyono', 'Desa Candimulyo', 'Jagung', 2.00, 42, '08133445566', 2);

-- --------------------------------------------------------

--
-- Struktur dari tabel `poktan`
--

CREATE TABLE `poktan` (
  `id_poktan` int(11) NOT NULL,
  `nama_poktan` varchar(150) NOT NULL,
  `ketua` varchar(100) DEFAULT NULL,
  `kelas` varchar(50) DEFAULT NULL,
  `id_gapoktan` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `poktan`
--

INSERT INTO `poktan` (`id_poktan`, `nama_poktan`, `ketua`, `kelas`, `id_gapoktan`) VALUES
(1, 'Poktan Subur Jaya', 'Budi Santoso', 'Madya', 1),
(2, 'Poktan Tani Harapan', 'Sukirno', 'Pemula', 2);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `gapoktan`
--
ALTER TABLE `gapoktan`
  ADD PRIMARY KEY (`id_gapoktan`),
  ADD KEY `id_lokasi` (`id_lokasi`);

--
-- Indeks untuk tabel `lokasi`
--
ALTER TABLE `lokasi`
  ADD PRIMARY KEY (`id_lokasi`);

--
-- Indeks untuk tabel `penyuluh`
--
ALTER TABLE `penyuluh`
  ADD PRIMARY KEY (`id_penyuluh`);

--
-- Indeks untuk tabel `petani`
--
ALTER TABLE `petani`
  ADD PRIMARY KEY (`id_petani`),
  ADD KEY `id_poktan` (`id_poktan`);

--
-- Indeks untuk tabel `poktan`
--
ALTER TABLE `poktan`
  ADD PRIMARY KEY (`id_poktan`),
  ADD KEY `id_gapoktan` (`id_gapoktan`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `gapoktan`
--
ALTER TABLE `gapoktan`
  MODIFY `id_gapoktan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT untuk tabel `lokasi`
--
ALTER TABLE `lokasi`
  MODIFY `id_lokasi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT untuk tabel `penyuluh`
--
ALTER TABLE `penyuluh`
  MODIFY `id_penyuluh` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT untuk tabel `petani`
--
ALTER TABLE `petani`
  MODIFY `id_petani` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT untuk tabel `poktan`
--
ALTER TABLE `poktan`
  MODIFY `id_poktan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `gapoktan`
--
ALTER TABLE `gapoktan`
  ADD CONSTRAINT `gapoktan_ibfk_1` FOREIGN KEY (`id_lokasi`) REFERENCES `lokasi` (`id_lokasi`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `petani`
--
ALTER TABLE `petani`
  ADD CONSTRAINT `petani_ibfk_1` FOREIGN KEY (`id_poktan`) REFERENCES `poktan` (`id_poktan`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `poktan`
--
ALTER TABLE `poktan`
  ADD CONSTRAINT `poktan_ibfk_1` FOREIGN KEY (`id_gapoktan`) REFERENCES `gapoktan` (`id_gapoktan`) ON DELETE SET NULL ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
