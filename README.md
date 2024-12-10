# Incident Response Toolkit

![License](https://img.shields.io/badge/license-MIT-blue)
![Python Version](https://img.shields.io/badge/python-3.10-blue)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20macos-lightgrey)

**Incident Response Toolkit** adalah rangkaian alat otomatisasi untuk menangani insiden keamanan siber, yang dirancang untuk membantu tim respons insiden (IRT) dalam pengumpulan bukti, analisis, dan pelaporan.

## 🚀 Fitur Utama

- **Pengumpulan Bukti**  
  - **Memory Dump**: Mengambil snapshot memori aktif sistem.
  - **Disk Imaging**: Membuat citra disk yang dapat digunakan untuk analisis forensik.
  
- **Analisis Insiden**  
  - Deteksi IOC (Indicator of Compromise) secara otomatis.
  - Modul deteksi dan pengelompokan ancaman.

- **Pelaporan**  
  - Membuat laporan forensik terstruktur untuk kebutuhan dokumentasi.

## 🛠️ Instalasi
Pastikan Anda telah menginstal **Python 3.10+** di sistem Anda.

1. Clone repository:
```bash
   git clone https://github.com/defconpro/incident-response-toolkit.git
   cd incident-response-toolkit
```
2. Buat virtual environment (opsional, tetapi disarankan):
```
python3 -m venv venv
source venv/bin/activate  # Untuk Linux/MacOS
.\venv\Scripts\activate   # Untuk Windows
```
3. Instal dependensi:
```
pip install -r requirements.txt
```
## ⚡ Penggunaan
Menjalankan Toolkit Jalankan scripts utama:
```
python3 main.py
```
### Modul yang Tersedia
- **Memory Dump**
   - `python3 -m evidence_collector.memory_dump`
- **Disk Imaging**
   - `python3 -m evidence_collector.disk_imaging`
- IOC Detection
   - `python3 -m analysis_engine.ioc_detection`

## 🧩 Struktur Direktori
```
incident-response-toolkit/
├── analysis_engine/
│   ├── ioc_detection.py
├── evidence_collector/
│   ├── disk_imaging.py
│   ├── memory_dump.py
├── reporting_module/
│   ├── generate_report.py
├── main.py
├── requirements.txt
└── README.md
```

Dibuat dengan ❤️ oleh [M Faridl Romadani](https://github.com/zafranrayyan)






