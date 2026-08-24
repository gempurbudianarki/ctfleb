# 🛡️ CCA ARENA - Capture The Flag (CTFd)
> **Platform Kompetisi Keamanan Siber Resmi Diselenggarakan oleh CYBERSECURITY COMMUNITY OF ACEH (CCA)**

![CCA CTF Arena](CTFd/themes/gameboy-retro/static/img/logo_cca.png)

---

## 🎮 Tentang Platform

**CCA ARENA** adalah platform kompetisi **Capture The Flag (CTF)** berbasis framework CTFd yang telah dimodifikasi khusus dengan desain **Neo-Arcade / Game Boy Retro** bertema keamanan siber modern. Platform ini menyajikan pengalaman kompetisi yang interaktif, responsif, dan kaya estetika untuk komunitas siber Aceh dan seluruh Indonesia.

---

## ✨ Fitur Unggulan

- 🏛️ **Branding Komunitas CCA**: Terintegrasi penuh dengan identitas resmi Cybersecurity Community of Aceh.
- 🎨 **Tema Neo-Arcade & Pop-Cyber**:
  - Tampilan visual cerah dan berkarakter dengan kartu tantangan per kategori (Web, Crypto, Reverse, Pwn, Forensics, OSINT, Misc).
  - **Mode Terang & Gelap (Light / Dark Mode)** dengan kontras tinggi dan kenyamanan membaca maksimal.
  - Form input dan dropdown (*Select Box*) leluasa tanpa teks terpotong (*Zero-clipping guarantee*).
- 🔊 **Dual-Engine Retro Audio**:
  - Efek suara klik arcade Game Boy 8-Bit (*SFX*).
  - Musik latar belakang santai **Super Mario Bros. Overworld 8-Bit Chiptune** (*BGM*) dengan tombol ON/OFF dan *page-persistence*.
- ⚡ **Performa Kilat**:
  - Optimalisasi database SQLite dalam mode **WAL (Write-Ahead Logging)** dan in-memory caching.
  - Rendering grafik garis *Score Progression* yang cepat dan halus (*Quadratic Easing*).
- 👥 **Mendukung Mode Individu & Mode Tim (Team Mode)**:
  - Fleksibel untuk kompetisi individu maupun kerja sama kelompok (kapten tim, password tim, skor bersama).
- 🛡️ **Panel Admin Responsif**:
  - Dashboard manajemen soal, peserta, notifikasi, dan konfigurasi yang rapi dalam bilah navigasi modern.

---

## 🚀 Panduan Menjalankan Secara Lokal

### 1. Prasyarat
- Python 3.9 / 3.10 / 3.11
- Git

### 2. Instalasi & Menjalankan
```bash
# Clone repository
git clone https://github.com/gempurbudianarki/ctfleb.git
cd ctfleb

# Buat virtual environment (opsional tapi disarankan)
python -m venv env
# Windows:
.\env\Scripts\activate
# Linux/macOS:
source env/bin/activate

# Install dependensi
pip install -r requirements.txt

# Jalankan server
python serve.py --port 4000
```
Buka browser Anda di `http://127.0.0.1:4000/`.

---

## ☁️ Panduan Hosting di VPS (CloudPanel / Docker)

### Opsi A: Menggunakan CloudPanel (Python Site)
1. Di CloudPanel, pilih **Create a Python Site**.
2. Masukkan domain Anda (contoh: `ctf.domain.com`) dan pilih Python 3.10 / 3.11.
3. Upload seluruh file repository ini ke direktori root situs.
4. Jalankan `pip install -r requirements.txt` melalui SSH.
5. Konfigurasikan file service / Gunicorn dan aktifkan SSL gratis Let's Encrypt pada tab SSL/TLS.

### Opsi B: Menggunakan Docker Compose
```bash
docker compose up -d
```

---

## 📜 Lisensi & Atribusi
- Dibangun di atas open-source [CTFd](https://ctfd.io/).
- Dikelola dan dikembangkan oleh **Cybersecurity Community of Aceh (CCA)**.
