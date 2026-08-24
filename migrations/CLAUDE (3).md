# CLAUDE.md — CTFd Custom Theme: Retro Game Boy

Dokumen ini menjelaskan konteks dan spesifikasi desain UI/UX untuk custom theme CTFd bergaya retro Game Boy monokrom. Gunakan ini sebagai acuan utama saat membuat/mengedit theme.

## Konteks Proyek

- Platform: **CTFd** (open source, Apache 2.0), hasil clone dari `CTFd/CTFd`
- Tujuan: mengganti tampilan default CTFd (theme `core-beta`) dengan custom theme bertema **retro/game jadul**
- Struktur lomba 2 babak:
  - **Babak seleksi** (di CTFd ini): kategori standar CTF — Web, Crypto, Reverse, Pwn, Forensics, OSINT, Misc
  - **Babak final** (di luar CTFd, terpisah): miniatur IoT fisik (kamera, lampu, layar, audio) sebagai target hacking, tingkat kesulitan jauh lebih tinggi — gabungan teka-teki multi-vuln yang saling terkait
- Skala lomba: kampus/komunitas kecil (kurang dari 30 peserta)
- Struktur folder CTFd yang relevan: `CTFd/themes/<nama-theme>/` — berisi template Jinja2 (`templates/`), static assets (`static/css`, `static/js`, `static/img`)

## Konsep Desain: Game Boy Monokrom

Tema mengacu pada tampilan layar Game Boy klasik (1989) — palet hijau monokrom, resolusi rendah, font pixel, tanpa gradient/shadow blur modern.

### Palet Warna

| Nama | Hex | Penggunaan |
|---|---|---|
| GB Darkest | `#0F380F` | Teks utama, elemen ter-"gelap" |
| GB Dark | `#306230` | Border, elemen sekunder |
| GB Light | `#8BAC0F` | Aksen, hover state |
| GB Lightest | `#9BBC0F` | Background utama |

Catatan: hanya 4 warna ini yang dipakai secara konsisten di seluruh UI — tidak ada warna lain (no blue, no red) kecuali untuk indikator kritikal (misal error/alert boleh pakai merah pixel `#D93636` secukupnya, dipakai sangat jarang).

### Tipografi

- Font utama: **Press Start 2P** (judul, heading, tombol, scoreboard) — via Google Fonts
- Font sekunder/isi panjang: **VT323** (deskripsi challenge, body text) — lebih mudah dibaca dalam ukuran kecil dibanding Press Start 2P
- Semua teks: `text-transform: uppercase` untuk heading/label, huruf besar disjajarkan grid pixel
- Ukuran font dalam kelipatan genap (px), hindari sub-pixel rendering

### Prinsip Layout & Bentuk

- **No rounded corner** — semua elemen (card, button, modal) menggunakan sudut kotak tegas (`border-radius: 0`)
- **Border tebal** (3-4px solid) menggunakan warna GB Dark/Darkest, meniru garis pixel game jadul
- **Shadow pixelated**, bukan blur — gunakan teknik box-shadow bertingkat tanpa blur radius (contoh: `box-shadow: 4px 4px 0 #0F380F;`) untuk efek kedalaman ala sprite 8-bit
- Grid/spacing mengikuti kelipatan 8px (mendekati grid pixel art asli)
- Elemen interaktif (tombol, card challenge) punya efek "tekan" saat hover/klik: bergeser sedikit + shadow mengecil, meniru animasi tombol arcade

### Komponen Spesifik

**Challenge Card**
- Tampil seperti "menu select" game platformer: kotak dengan border tebal, ikon kategori pixel-art kecil di pojok (ikon disesuaikan per kategori: Web, Crypto, Reverse, Pwn, Forensics, OSINT, Misc)
- Status "solved" ditandai efek highlight hijau terang (GB Light) + border berubah warna
- Poin ditampilkan dengan font Press Start 2P, posisi pojok kanan atas card

**Scoreboard**
- Didesain meniru layar **"HIGH SCORE"** arcade klasik: list ranking dengan nomor urut besar, nama tim/peserta rata kiri, skor rata kanan, semua pakai font Press Start 2P
- Baris ranking 1-3 (podium) diberi indikator kecil (misal ikon bintang/mahkota pixel) tanpa keluar dari palet warna
- Background scrollable area tetap GB Lightest, garis pemisah antar baris pakai GB Dark solid tipis

**Navbar & Layout Umum**
- Navbar bergaya "status bar" game — flat, border bawah tebal, logo/judul event di kiri pakai Press Start 2P
- Background halaman: GB Lightest solid (tanpa gradient/texture)
- Modal/dialog: border tebal + shadow pixelated, tombol "close" bergaya pixel (kotak X sederhana, bukan icon modern)

**Sound (opsional, tahap lanjut)**
- Efek suara 8-bit pendek (`.wav`/`.ogg` kecil) untuk event solve challenge dan notifikasi — opsional, tidak wajib di iterasi pertama

## Prioritas Implementasi

1. Setup palet warna + font di CSS variables (`:root`)
2. Override komponen dasar: navbar, card, button, modal
3. Kustomisasi halaman scoreboard (prioritas tinggi — paling sering dilihat peserta)
4. Kustomisasi halaman challenge (card + detail modal)
5. (Opsional) efek suara & animasi sprite kecil

## Alur Rilis Soal (Challenge Release)

Soal tidak dipublikasikan sekaligus — mengikuti pola umum lomba CTF, soal dirilis bertahap sesuai kontrol admin.

- Semua challenge dibuat dalam kondisi **Hidden** terlebih dahulu di CTFd
- Admin mengubah status menjadi **Visible** satu per satu sesuai jadwal yang ditentukan
- Opsional: bisa memakai fitur **Requirements** (unlock chain) di CTFd — soal berikutnya baru muncul setelah soal tertentu ke-solve
- Opsional lanjutan: rilis otomatis by jadwal via script (memakai CTFd Admin API + cron), bukan fitur bawaan CTFd

## Referensi Visual

- Estetika: layar Game Boy original (1989), palet hijau monokrom 4 warna
- Referensi tambahan: layar "HIGH SCORE" arcade klasik untuk struktur scoreboard
- Hindari: gradient modern, shadow blur, rounded corner, warna di luar palet 4-warna (kecuali indikator kritikal minor)
