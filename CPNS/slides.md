---
theme: seriph
background: https://images.unsplash.com/photo-1497215728101-856f4ea42174?q=80&w=1920&auto=format&fit=crop
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Seminar Rancangan Aktualisasi Latsar CPNS 2026
drawings:
  persist: false
transition: fade
title: Rancangan Aktualisasi CPNS 2026
---

# Rancangan Aktualisasi
**Pelatihan Dasar CPNS Angkatan VI Tahun 2026**

<div v-motion
  :initial="{ y: 50, opacity: 0 }"
  :enter="{ y: 0, opacity: 1, transition: { duration: 800, delay: 200 } }"
  class="mt-8 text-xl font-semibold text-blue-900 bg-white/95 p-6 rounded-xl shadow-2xl border border-white/50 backdrop-blur-md inline-block">
Pengembangan Sistem Dashboard Analitik Tridharma Berbasis SINTA (SINTA Intel)<br/>
pada Lab Inovasi Digital Prodi SI FSTI ITK
</div>

<div v-motion
  :initial="{ scale: 0.8, opacity: 0 }"
  :enter="{ scale: 1, opacity: 1, transition: { duration: 500, delay: 800 } }"
  class="mt-12 text-sm text-gray-900 bg-white/80 inline-block px-6 py-3 rounded-full shadow-md font-medium border border-white/50 backdrop-blur-sm">
Disusun Oleh: <b class="text-blue-800">Aidil Saputra Kirsan, S.ST., M.Tr.Kom</b>
</div>

---
layout: two-cols
---

# 2. Profil Instansi
**Institut Teknologi Kalimantan (ITK)**

Kampus teknologi yang unggul di wilayah Tengah dan Timur Indonesia, berlokasi di Balikpapan, Kalimantan Timur.

<br>

<v-clicks>

- **Status:** Perguruan Tinggi Negeri (PTN)
- **Akreditasi:** B (BAN-PT)
- **Fokus Riset:** Energi, Smart City, Kemaritiman, Teknologi Pangan

</v-clicks>

::right::

<div class="mt-12 ml-8 p-6 bg-blue-50/50 rounded-xl border-l-4 border-blue-600 shadow-sm" v-click>
<b>Visi ITK:</b>
<p class="mt-4 text-sm text-gray-700 leading-relaxed">
Menjadi perguruan tinggi unggul dan berperan aktif dalam pembangunan nasional melalui pemberdayaan potensi daerah Kalimantan.
</p>
</div>

---
layout: center
---

# 3. Profil Peserta & Jabatan

<div class="grid grid-cols-2 gap-8 mt-8 text-left">
  <div v-motion
    :initial="{ x: -50, opacity: 0 }"
    :enter="{ x: 0, opacity: 1, transition: { duration: 500 } }"
    class="bg-white/60 p-6 rounded-xl shadow-md border border-gray-100 hover:shadow-lg hover:-translate-y-1 transition-all">
    <div class="text-blue-600 mb-2"><i class="fas fa-user-circle text-2xl animate-pulse"></i></div>
    <div class="font-bold text-lg mb-1">Aidil Saputra Kirsan, S.ST., M.Tr.Kom</div>
    <div class="text-sm text-gray-500">NIP. 199403172025061004</div>
  </div>
  
  <div v-motion
    :initial="{ x: 50, opacity: 0 }"
    :enter="{ x: 0, opacity: 1, transition: { duration: 500, delay: 200 } }"
    class="bg-white/60 p-6 rounded-xl shadow-md border border-gray-100 hover:shadow-lg hover:-translate-y-1 transition-all">
    <div class="text-blue-600 mb-2"><i class="fas fa-briefcase text-2xl animate-bounce"></i></div>
    <div class="font-bold text-lg mb-1">Dosen Asisten Ahli</div>
    <div class="text-sm text-gray-500">Kepala Lab Inovasi Digital<br/>Prodi Sistem Informasi, FSTI ITK</div>
  </div>
</div>

---
layout: default
---

# 4. Identifikasi Isu

Berdasarkan analisis situasi di unit kerja, ditemukan 3 isu utama:

<v-clicks>

1. **Belum Ada Sistem Digital Pengelolaan Tugas Akhir/Skripsi Mahasiswa (SIM TA)**
   <div class="text-sm text-gray-500 ml-6 mb-4">Proses masih manual, rawan kehilangan data, dan pemantauan progres sulit dilakukan.</div>

2. <span class="text-red-600 font-bold">Data Riset & Publikasi Dosen Tidak Terkelola Terpusat</span>
   <div class="text-sm text-gray-500 ml-6 mb-4">Data tersebar di berbagai platform tanpa agregasi, menyulitkan pemetaan riset dan persiapan akreditasi BAN-PT.</div>

3. **Belum Ada Sistem Evaluasi Kepuasan Layanan Akademik Mahasiswa Secara Digital**
   <div class="text-sm text-gray-500 ml-6">Pengumpulan umpan balik masih sporadis, data sulit dianalisis pimpinan untuk tindak lanjut.</div>

</v-clicks>

---
layout: statement
---

# 5. Isu Terpilih

Data Riset & Publikasi Dosen<br/>Tidak Terkelola Terpusat

---
layout: center
---

# 6. Analisis Isu (USG)

Penetapan Isu menggunakan metode **Urgency, Seriousness, Growth (USG)**:

| Isu Aktual | U | S | G | Total | Prioritas |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Belum Ada Sistem Digital Pengelolaan TA (SIM TA) | 4 | 4 | 3 | 11 | II |
| **Data Riset & Publikasi Dosen Tidak Terkelola Terpusat** | **5** | **5** | **4** | **14** | **I** |
| Belum Ada Sistem Evaluasi Kepuasan Layanan Digital | 3 | 3 | 3 | 9 | III |

*Alasan Isu Terpilih:* Sangat mendesak karena jadwal akreditasi semakin dekat, sangat berdampak pada nilai akreditasi prodi, dan akan semakin rumit seiring bertambahnya volume publikasi.

---
layout: default
---

# 7. Keterkaitan Isu dengan Agenda III

Isu terpilih sangat erat kaitannya dengan peran dan kedudukan PNS dalam mewujudkan **Smart Governance**:

<div class="grid grid-cols-2 gap-6 mt-8">
  <div class="bg-blue-50 p-6 rounded-lg border border-blue-100" v-click>
    <h3 class="text-blue-800 font-bold border-b border-blue-200 pb-2 mb-3">Smart ASN</h3>
    <p class="text-sm text-gray-700">Pengelolaan data yang manual mencerminkan kesenjangan <i>digital skill</i>. Solusi digital (SINTA Intel) mengatasi hal ini dengan pemanfaatan teknologi Machine Learning dan Web Development.</p>
  </div>
  
  <div class="bg-green-50 p-6 rounded-lg border border-green-100" v-click>
    <h3 class="text-green-800 font-bold border-b border-green-200 pb-2 mb-3">Manajemen ASN</h3>
    <p class="text-sm text-gray-700">Secara akuntabilitas, ASN Dosen wajib membuktikan kinerja Tridharma secara terukur. Ketiadaan sistem terpusat menghambat hal ini. Solusinya memberikan data transparan dan terverifikasi.</p>
  </div>
</div>

---
layout: default
transition: slide-up
---

# 8. Analisis Akar Masalah (Fishbone)

<div v-motion
  :initial="{ opacity: 0, scale: 0.9 }"
  :enter="{ opacity: 1, scale: 1, transition: { duration: 600 } }"
  class="flex justify-center mt-6">
  <img src="./fishbone.png" alt="Fishbone Diagram" class="w-full h-[70vh] object-contain drop-shadow-xl rounded-xl" />
</div>

---
layout: default
---

# 9. Tujuan, Manfaat, & Ruang Lingkup

<div class="grid grid-cols-3 gap-4 mt-6">
  <div v-motion :initial="{ y: 50, opacity: 0 }" :enter="{ y: 0, opacity: 1, transition: { delay: 100 } }" class="bg-white/90 p-5 border-t-4 border-blue-500 rounded-lg shadow-md hover:-translate-y-2 transition-transform duration-300">
    <h3 class="font-bold text-blue-700 mb-2 flex items-center gap-2"><i class="fas fa-bullseye text-blue-400"></i> Tujuan</h3>
    <ul class="text-xs space-y-2 text-gray-700 list-disc ml-4">
      <li>Membangun SINTA Intel (Dashboard Analitik).</li>
      <li>Menyediakan pemetaan riset & deteksi kolaborasi via AI.</li>
      <li>Monitoring dana riset (Funding Dashboard).</li>
      <li>Menyediakan data rasio DTPS otomatis untuk Akreditasi.</li>
    </ul>
  </div>
  
  <div v-motion :initial="{ y: 50, opacity: 0 }" :enter="{ y: 0, opacity: 1, transition: { delay: 300 } }" class="bg-white/90 p-5 border-t-4 border-green-500 rounded-lg shadow-md hover:-translate-y-2 transition-transform duration-300">
    <h3 class="font-bold text-green-700 mb-2 flex items-center gap-2"><i class="fas fa-gift text-green-400"></i> Manfaat</h3>
    <ul class="text-xs space-y-2 text-gray-700 list-disc ml-4">
      <li><b>Penulis:</b> Aktualisasi teknis & BerAKHLAK.</li>
      <li><b>Prodi:</b> Efisiensi data & kesiapan akreditasi akurat.</li>
      <li><b>ITK:</b> Akuntabilitas kinerja Tridharma terbukti.</li>
      <li><b>Ekosistem:</b> Mendorong kolaborasi riset interdisipliner.</li>
    </ul>
  </div>
  
  <div v-motion :initial="{ y: 50, opacity: 0 }" :enter="{ y: 0, opacity: 1, transition: { delay: 500 } }" class="bg-white/90 p-5 border-t-4 border-purple-500 rounded-lg shadow-md hover:-translate-y-2 transition-transform duration-300">
    <h3 class="font-bold text-purple-700 mb-2 flex items-center gap-2"><i class="fas fa-expand-arrows-alt text-purple-400"></i> Ruang Lingkup</h3>
    <ul class="text-xs space-y-2 text-gray-700 list-disc ml-4">
      <li><b>Sasaran:</b> Dosen Prodi SI & Bisnis Digital.</li>
      <li><b>Lokasi:</b> Lab Inovasi Digital ITK.</li>
      <li><b>Sumber Data:</b> Data SINTA Kemdiktisaintek & Hibah BIMA.</li>
    </ul>
  </div>
</div>

---
layout: default
---

# 10. Kegiatan Aktualisasi (Kaitan Agenda III)

Terdapat 5 Kegiatan Utama yang dilandasi nilai Smart ASN & Manajemen ASN:

<br>

<v-clicks>

1. **Pemetaan & Pengumpulan Data Dosen** *(Manajemen ASN: Akuntabilitas Data)*
2. **Pengembangan Pipeline Scraper Otomatis** *(Smart ASN: Literasi Digital & Inovasi)*
3. **Implementasi Fitur Analytics & Dashboard AI** *(Smart ASN & Manajemen ASN)*
4. **Implementasi Dashboard Akreditasi & Funding** *(Manajemen ASN: Kinerja Institusi)*
5. **Deployment, Sosialisasi & Evaluasi Sistem** *(Smart ASN & Manajemen ASN)*

</v-clicks>

---
layout: center
---

# 11. Matrik Kegiatan & Nilai Dasar (Ringkasan)

Nilai-nilai dasar **BerAKHLAK** diimplementasikan pada setiap tahapan:

<div class="text-sm bg-gray-50 p-6 rounded-xl border mt-6">
  <b>Kegiatan Inti: Pengembangan Modul SINTA Intel</b>
  <ul class="mt-3 space-y-2 list-disc ml-6 text-gray-700">
    <li><b>Berorientasi Pelayanan:</b> Otomasi data mempercepat pimpinan mendapat laporan.</li>
    <li><b>Akuntabel:</b> Algoritma scraping & AI Clustering dapat diverifikasi dan diaudit.</li>
    <li><b>Kompeten:</b> Penggunaan Python, React/Vue, & Machine Learning (TF-IDF/K-Means).</li>
    <li><b>Harmonis:</b> Solusi mengakomodasi kebutuhan lintas prodi (SI & Bisnis Digital).</li>
    <li><b>Loyal:</b> Berkontribusi langsung pada nilai akreditasi institusi ITK.</li>
    <li><b>Adaptif:</b> Memanfaatkan AI/NLP untuk menyelesaikan masalah pendataan.</li>
    <li><b>Kolaboratif:</b> Bekerja sama dengan Kaprodi, Wakil Dekan, dan Tim Mutu FSTI.</li>
  </ul>
</div>

---
layout: default
---

# 12. Jadwal Pelaksanaan (12 Minggu)

Pelaksanaan aktualisasi (24 Februari 2026 s.d. 24 Mei 2026):

<div class="mt-6 text-sm">

| Kegiatan Utama | Bulan 1 (M1-M4) | Bulan 2 (M5-M8) | Bulan 3 (M9-M12) |
| :--- | :--- | :--- | :--- |
| **1. Pemetaan & Pengumpulan Data** | Minggu 1 - 2 | | |
| **2. Pipeline Scraper Otomatis** | Minggu 2 - 4 | | |
| **3. Implementasi Analytics & Dashboard** | | Minggu 4 - 8 | |
| **4. Fitur Akreditasi (DTPS & Funding)** | | Minggu 7 - 8 | Minggu 9 - 10 |
| **5. Deployment, Sosialisasi, Evaluasi** | | | Minggu 10 - 12 |

</div>

<div class="mt-12 text-center text-gray-500 italic">
"Transformasi Digital untuk Akuntabilitas Tridharma Perguruan Tinggi"
</div>

---
layout: center
class: text-center
---

# Terima Kasih
**Mohon Arahan dan Masukannya**
