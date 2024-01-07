-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 07 Jan 2024 pada 17.27
-- Versi server: 10.4.24-MariaDB
-- Versi PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tugas_alpro`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `alpro`
--

CREATE TABLE `alpro` (
  `id` int(11) NOT NULL,
  `nama_barang` varchar(50) NOT NULL,
  `jumlah` int(10) NOT NULL,
  `satuan` varchar(10) NOT NULL,
  `harga` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `alpro`
--

INSERT INTO `alpro` (`id`, `nama_barang`, `jumlah`, `satuan`, `harga`) VALUES
(10001, 'Kursi', 5, 'Unit', 8700000),
(10002, 'Meja', 3, 'Unit', 4000000),
(10003, 'Layar Monitor', 1, 'Unit', 6500000),
(10004, 'Mikrotik', 3, 'Unit', 850000),
(10005, 'Keyboard', 3, 'Unit', 700000);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `alpro`
--
ALTER TABLE `alpro`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `alpro`
--
ALTER TABLE `alpro`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101113;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
