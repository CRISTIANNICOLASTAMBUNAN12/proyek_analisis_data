Analisis Penyaluran Kredit - Aplikasi Streamlit

Ini adalah aplikasi Streamlit yang menganalisis dan memvisualisasikan data terkait Penyaluran Kredit. Aplikasi ini menyediakan berbagai analisis statistik, visualisasi, dan wawasan berdasarkan data yang dimuat dari file Excel.

Fitur
Statistik deskriptif dari data penyaluran kredit.

Analisis nilai yang hilang (missing values).

Visualisasi seperti grafik batang, plot sebar, heatmap, dan plot geografis.

Filter interaktif berdasarkan provinsi.

Persyaratan Untuk menjalankan aplikasi ini, Anda perlu menginstal dependensi yang diperlukan. Ini termasuk pustaka untuk manipulasi data, visualisasi, dan Streamlit untuk membangun aplikasi web.

Pustaka Python yang Dibutuhkan
pandas: Untuk menangani data.
matplotlib: Untuk visualisasi statis.
seaborn: Untuk visualisasi statistik yang lebih baik.
plotly: Untuk plot interaktif, terutama visualisasi geografis.
openpyxl: Untuk membaca file Excel.
Anda dapat menginstal semua dependensi yang diperlukan menggunakan pip dengan menjalankan:

bash
Salin kode
pip install -r requirements.txt
Berikut adalah isi dari requirements.txt:

txt
Salin kode
pandas>=2.2.3
matplotlib>=3.9.2
seaborn>=0.13.2
plotly>=5.0.0
openpyxl>=3.0.0
streamlit>=1.30.0
scikit-learn>=1.5.2
Pengaturan dan Menjalankan Aplikasi
Clone atau Unduh Repository: Unduh atau clone repository ini ke mesin lokal Anda.

bash
Salin kode
git clone <repository_url>
Letakkan File Excel: Pastikan file Excel (misalnya workhome.xlsx) yang berisi data penyaluran kredit diletakkan di direktori yang sama dengan skrip Python (sda.py).

Catatan: Jika file berada di lokasi lain, perbarui path-nya di kode sesuai dengan lokasi file.

Jalankan Aplikasi Streamlit: Setelah menginstal dependensi dan menyiapkan file data, buka terminal dan arahkan ke direktori tempat skrip Python (sda.py) berada, lalu jalankan perintah berikut:

bash
Salin kode
streamlit run sda.py
Buka Aplikasi: Setelah menjalankan perintah di atas, Streamlit akan memulai aplikasi dan memberikan URL lokal di terminal. Buka URL tersebut di browser untuk berinteraksi dengan aplikasi.

URL default biasanya http://localhost:8501.
