---
theme: seriph
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
  class="mt-8 text-xl font-semibold text-blue-900 dark:text-blue-100 bg-white/95 dark:bg-slate-900/90 p-6 rounded-xl shadow-2xl border border-white/50 dark:border-slate-700 backdrop-blur-md inline-block">
Pengembangan Sistem Dashboard Analitik Tridharma Berbasis SINTA (SINTA Intel)<br/>
pada Lab Inovasi Digital Prodi SI FSTI ITK
</div>

<div v-motion
  :initial="{ scale: 0.8, opacity: 0 }"
  :enter="{ scale: 1, opacity: 1, transition: { duration: 500, delay: 800 } }"
  class="mt-12 text-sm text-gray-900 dark:text-gray-100 bg-white/80 dark:bg-slate-800/80 inline-block px-6 py-3 rounded-full shadow-md font-medium border border-white/50 dark:border-slate-700 backdrop-blur-sm">
Disusun Oleh: <b class="text-blue-800 dark:text-blue-400">Aidil Saputra Kirsan, S.ST., M.Tr.Kom</b>
</div>

---
layout: center
---

# Outline Presentasi

<div class="grid grid-cols-2 gap-4 mt-8 text-left">

  <div v-click class="bg-white/80 dark:bg-slate-800/80 p-4 rounded-xl border-l-4 border-blue-500 shadow-md flex gap-4 items-start">
    <div class="bg-blue-100 dark:bg-blue-900/50 rounded-lg p-2 text-blue-600 dark:text-blue-400 flex-shrink-0">
      <i class="fas fa-user-shield text-xl"></i>
    </div>
    <div>
      <div class="font-bold text-blue-800 dark:text-blue-300 text-sm mb-1">Agenda 1–3 · Nilai Dasar ASN</div>
      <p class="text-xs text-gray-600 dark:text-gray-400">Bela Negara, BerAKHLAK, Smart Governance & Manajemen ASN</p>
    </div>
  </div>

  <div v-click class="bg-white/80 dark:bg-slate-800/80 p-4 rounded-xl border-l-4 border-amber-500 shadow-md flex gap-4 items-start">
    <div class="bg-amber-100 dark:bg-amber-900/50 rounded-lg p-2 text-amber-600 dark:text-amber-400 flex-shrink-0">
      <i class="fas fa-magnifying-glass-chart text-xl"></i>
    </div>
    <div>
      <div class="font-bold text-amber-800 dark:text-amber-300 text-sm mb-1">Identifikasi & Analisis Isu</div>
      <p class="text-xs text-gray-600 dark:text-gray-400">Metode USG, Fishbone, penetapan isu terpilih</p>
    </div>
  </div>

  <div v-click class="bg-white/80 dark:bg-slate-800/80 p-4 rounded-xl border-l-4 border-indigo-500 shadow-md flex gap-4 items-start">
    <div class="bg-indigo-100 dark:bg-indigo-900/50 rounded-lg p-2 text-indigo-600 dark:text-indigo-400 flex-shrink-0">
      <i class="fas fa-microchip text-xl"></i>
    </div>
    <div>
      <div class="font-bold text-indigo-800 dark:text-indigo-300 text-sm mb-1">Gagasan Kreatif · SINTA Intel</div>
      <p class="text-xs text-gray-600 dark:text-gray-400">Tujuan, manfaat, kondisi before/after, 7 fitur utama</p>
    </div>
  </div>

  <div v-click class="bg-white/80 dark:bg-slate-800/80 p-4 rounded-xl border-l-4 border-green-500 shadow-md flex gap-4 items-start">
    <div class="bg-green-100 dark:bg-green-900/50 rounded-lg p-2 text-green-600 dark:text-green-400 flex-shrink-0">
      <i class="fas fa-list-check text-xl"></i>
    </div>
    <div>
      <div class="font-bold text-green-800 dark:text-green-300 text-sm mb-1">Rencana Aktualisasi</div>
      <p class="text-xs text-gray-600 dark:text-gray-400">5 kegiatan, jadwal 7 minggu, output & deliverables</p>
    </div>
  </div>

</div>

---
layout: two-cols
---

# Profil Instansi
**Institut Teknologi Kalimantan (ITK)**

Satu-satunya Institut Teknologi Negeri di wilayah Tengah dan Timur Indonesia, berlokasi di Balikpapan, Kalimantan Timur.

<br>

<v-clicks>

- **Dasar Hukum:** Perpres No. 125 Tahun 2014
- **Akreditasi:** B (BAN-PT)
- **Fokus Riset:** Energi, Smart City, Kemaritiman, Tek. Pangan
- **Rektor:** Prof. Dr. rer. nat. Agus Rubiyanto, M.Eng.Sc.

</v-clicks>

::right::

<div class="mt-12 ml-8 p-6 bg-blue-50/80 dark:bg-blue-900/40 rounded-xl border-l-4 border-blue-600 shadow-sm" v-click>
<b>Visi ITK:</b>
<p class="mt-4 text-sm text-gray-700 dark:text-gray-200 leading-relaxed">
Menjadi perguruan tinggi unggul dan berperan aktif dalam pembangunan nasional melalui pemberdayaan potensi daerah Kalimantan.
</p>
</div>

<div class="mt-4 ml-8 p-6 bg-green-50/80 dark:bg-emerald-900/30 rounded-xl border-l-4 border-green-600 shadow-sm" v-click>
<b>Misi:</b>
<p class="mt-2 text-sm text-gray-700 dark:text-gray-200 leading-relaxed">
Menyelenggarakan Tridharma PT bermutu · Menghasilkan lulusan unggul · Membangun kerja sama dengan pemangku kepentingan.
</p>
</div>

---
layout: center
---

# Profil Peserta & Jabatan

<div class="grid grid-cols-2 gap-8 mt-8 text-left">
  <div v-motion
    :initial="{ x: -50, opacity: 0 }"
    :enter="{ x: 0, opacity: 1, transition: { duration: 500 } }"
    class="bg-white/60 dark:bg-slate-800/80 p-6 rounded-xl shadow-md border border-gray-100 dark:border-slate-700">
    <div class="text-blue-600 dark:text-blue-400 mb-2"><i class="fas fa-user-circle text-2xl"></i></div>
    <div class="font-bold text-lg mb-1 dark:text-gray-100">Aidil Saputra Kirsan, S.ST., M.Tr.Kom</div>
    <div class="text-sm text-gray-500 dark:text-gray-400">NIP. 199403172025061004</div>
    <div class="text-xs text-gray-400 dark:text-gray-500 mt-2">Penata Muda Tk.I / III-b</div>
  </div>
  
  <div v-motion
    :initial="{ x: 50, opacity: 0 }"
    :enter="{ x: 0, opacity: 1, transition: { duration: 500, delay: 200 } }"
    class="bg-white/60 dark:bg-slate-800/80 p-6 rounded-xl shadow-md border border-gray-100 dark:border-slate-700">
    <div class="text-blue-600 dark:text-blue-400 mb-2"><i class="fas fa-briefcase text-2xl"></i></div>
    <div class="font-bold text-lg mb-1 dark:text-gray-100">Dosen Asisten Ahli / Ka. Lab</div>
    <div class="text-sm text-gray-500 dark:text-gray-400">Lab Inovasi Digital<br/>Prodi Sistem Informasi, FSTI ITK</div>
  </div>
</div>

<div class="mt-6 grid grid-cols-3 gap-4 text-center text-sm" v-click>
  <div class="bg-blue-50/80 dark:bg-slate-800 p-3 rounded-lg border dark:border-slate-700">
    <div class="font-bold text-blue-700 dark:text-blue-400">Mentor</div>
    <div class="text-gray-600 dark:text-gray-400 text-xs mt-1">Irma Fitria, S.Si., M.Si</div>
  </div>
  <div class="bg-blue-50/80 dark:bg-slate-800 p-3 rounded-lg border dark:border-slate-700">
    <div class="font-bold text-blue-700 dark:text-blue-400">Coach</div>
    <div class="text-gray-600 dark:text-gray-400 text-xs mt-1">Mustari Kurniawati, S.IP., MPA</div>
  </div>
  <div class="bg-blue-50/80 dark:bg-slate-800 p-3 rounded-lg border dark:border-slate-700">
    <div class="font-bold text-blue-700 dark:text-blue-400">Habituasi</div>
    <div class="text-gray-600 dark:text-gray-400 text-xs mt-1">7 Maret – 22 April 2026 · 7 Minggu</div>
  </div>
</div>

---
layout: default
---

# Agenda 1 — Sikap Perilaku Bela Negara

Bela Negara bukan sekadar urusan militer, melainkan **tekad, sikap, dan perilaku warga negara** yang dijiwai kecintaan terhadap NKRI.

<div class="grid grid-cols-3 gap-3 mt-6">
  <div class="bg-white/90 dark:bg-slate-800/90 p-4 rounded-lg border-t-3 border-blue-500 shadow-sm text-center" v-click>
    <div class="text-2xl mb-2">🇮🇩</div>
    <div class="font-bold text-sm text-blue-700 dark:text-blue-400 mb-1">Cinta Tanah Air</div>
    <p class="text-xs text-gray-600 dark:text-gray-400">Kebanggaan mengabdi sebagai ASN Dosen di PTN yang memajukan pendidikan di Kalimantan</p>
  </div>
  <div class="bg-white/90 dark:bg-slate-800/90 p-4 rounded-lg border-t-3 border-green-500 shadow-sm text-center" v-click>
    <div class="text-2xl mb-2">🤝</div>
    <div class="font-bold text-sm text-green-700 dark:text-emerald-400 mb-1">Sadar Berbangsa & Bernegara</div>
    <p class="text-xs text-gray-600 dark:text-gray-400">Menghormati keberagaman dan berkontribusi aktif pada pembangunan nasional</p>
  </div>
  <div class="bg-white/90 dark:bg-slate-800/90 p-4 rounded-lg border-t-3 border-purple-500 shadow-sm text-center" v-click>
    <div class="text-2xl mb-2">⭐</div>
    <div class="font-bold text-sm text-purple-700 dark:text-purple-400 mb-1">Setia Kepada Pancasila</div>
    <p class="text-xs text-gray-600 dark:text-gray-400">Menjadikan Pancasila sebagai landasan dalam setiap keputusan</p>
  </div>
</div>

<div class="grid grid-cols-2 gap-3 mt-3">
  <div class="bg-white/90 dark:bg-slate-800/90 p-4 rounded-lg border-t-3 border-red-500 shadow-sm text-center" v-click>
    <div class="text-2xl mb-2">🛡️</div>
    <div class="font-bold text-sm text-red-700 dark:text-red-400 mb-1">Rela Berkorban</div>
    <p class="text-xs text-gray-600 dark:text-gray-400">Mendahulukan kepentingan institusi; membangun SINTA Intel melebihi tugas pokok</p>
  </div>
  <div class="bg-white/90 dark:bg-slate-800/90 p-4 rounded-lg border-t-3 border-amber-500 shadow-sm text-center" v-click>
    <div class="text-2xl mb-2">💪</div>
    <div class="font-bold text-sm text-amber-700 dark:text-amber-400 mb-1">Kemampuan Bela Negara</div>
    <p class="text-xs text-gray-600 dark:text-gray-400">Menggunakan keahlian IT untuk transformasi layanan publik</p>
  </div>
</div>

---
layout: default
---

# Agenda 2 — Nilai Dasar ASN BerAKHLAK

Tujuh nilai inti ASN yang diimplementasikan dalam aktualisasi:

<div class="grid grid-cols-4 gap-2 mt-6 text-center">
  <div class="bg-blue-600 text-white p-3 rounded-lg shadow-md" v-click>
    <div class="text-2xl font-bold opacity-30 absolute -top-1 right-2">B</div>
    <div class="font-bold text-xs">Berorientasi Pelayanan</div>
    <p class="text-[10px] mt-1 opacity-80">SINTA Intel mempercepat akses data Tridharma bagi pimpinan</p>
  </div>
  <div class="bg-indigo-700 text-white p-3 rounded-lg shadow-md" v-click>
    <div class="font-bold text-xs">Akuntabel</div>
    <p class="text-[10px] mt-1 opacity-80">Kalkulasi rasio DTPS otomatis & terverifikasi</p>
  </div>
  <div class="bg-teal-600 text-white p-3 rounded-lg shadow-md" v-click>
    <div class="font-bold text-xs">Kompeten</div>
    <p class="text-[10px] mt-1 opacity-80">Penggunaan Python, Vue.js & ML (TF-IDF/K-Means)</p>
  </div>
  <div class="bg-purple-600 text-white p-3 rounded-lg shadow-md" v-click>
    <div class="font-bold text-xs">Harmonis</div>
    <p class="text-[10px] mt-1 opacity-80">Mengakomodasi kebutuhan 2 prodi (SI & Bisnis Digital)</p>
  </div>
</div>

<div class="grid grid-cols-3 gap-2 mt-2 text-center">
  <div class="bg-pink-600 text-white p-3 rounded-lg shadow-md" v-click>
    <div class="font-bold text-xs">Loyal</div>
    <p class="text-[10px] mt-1 opacity-80">Berkontribusi langsung pada nilai akreditasi BAN-PT institusi</p>
  </div>
  <div class="bg-orange-600 text-white p-3 rounded-lg shadow-md" v-click>
    <div class="font-bold text-xs">Adaptif</div>
    <p class="text-[10px] mt-1 opacity-80">Memanfaatkan AI/NLP dan data engineering untuk menyelesaikan masalah</p>
  </div>
  <div class="bg-green-600 text-white p-3 rounded-lg shadow-md" v-click>
    <div class="font-bold text-xs">Kolaboratif</div>
    <p class="text-[10px] mt-1 opacity-80">Kerja sama dengan Kaprodi, Wakil Dekan, Tim Mutu FSTI</p>
  </div>
</div>

---
layout: default
---

# Agenda 3 — Smart Governance & Manajemen ASN

Isu terpilih sangat erat kaitannya dengan peran dan kedudukan PNS dalam mewujudkan **Smart Governance**:

<div class="grid grid-cols-2 gap-6 mt-8">
  <div class="bg-blue-50 dark:bg-slate-800 p-6 rounded-lg border border-blue-100 dark:border-slate-700" v-click>
    <h3 class="text-blue-800 dark:text-blue-400 font-bold border-b border-blue-200 dark:border-slate-600 pb-2 mb-3"><i class="fas fa-microchip mr-2"></i>Smart ASN</h3>
    <p class="text-sm text-gray-700 dark:text-gray-300">Penulis tidak sekadar menggunakan teknologi, melainkan <i>menciptakan</i> solusi digital inovatif berbasis ML dan data engineering — manifestasi nyata profil Smart ASN.</p>
  </div>
  
  <div class="bg-green-50 dark:bg-emerald-900/30 p-6 rounded-lg border border-green-100 dark:border-slate-700" v-click>
    <h3 class="text-green-800 dark:text-emerald-400 font-bold border-b border-green-200 dark:border-slate-600 pb-2 mb-3"><i class="fas fa-chart-bar mr-2"></i>Manajemen ASN</h3>
    <p class="text-sm text-gray-700 dark:text-gray-300">ASN Dosen wajib membuktikan kinerja Tridharma secara terukur. SINTA Intel mendukung implementasi Manajemen ASN yang akuntabel, transparan, dan berbasis data.</p>
  </div>
</div>

---
layout: default
---

# Identifikasi Isu

Berdasarkan analisis situasi di unit kerja, ditemukan **3 isu aktual**:

<v-clicks>

1. **Pengelolaan Tugas Akhir/Skripsi Mahasiswa FSTI ITK Belum Efektif**
   <div class="text-sm text-gray-500 ml-6 mb-4">Proses manual via berkas fisik; dokumen TA tidak terkelola dengan baik; admin kesulitan mengelola administrasi dan penjadwalan sidang.</div>

2. <span class="text-red-600 font-bold">Pengelolaan Data Riset & Pengabdian Dosen Belum Terpusat dan Teranalisis</span>
   <div class="text-sm text-gray-500 ml-6 mb-4">Data tersebar di SINTA, Scopus, GScholar tanpa agregasi. Peta riset tidak terbaca; nilai akreditasi prodi terdampak langsung.</div>

3. **Umpan Balik Mahasiswa terhadap Layanan Akademik Belum Digital**
   <div class="text-sm text-gray-500 ml-6">Pengumpulan sporadis via kuesioner kertas yang tidak terintegrasi.</div>

</v-clicks>

---
layout: statement
---

# Isu Terpilih

Pengelolaan Data Riset & Pengabdian Dosen<br/>di Lab Inovasi Digital Belum Terpusat<br/>dan Teranalisis

---
layout: center
---

# Analisis Isu — Metode USG

Penetapan isu menggunakan metode **Urgency, Seriousness, Growth (USG)**:

<div v-motion
  :initial="{ opacity: 0, y: 30 }"
  :enter="{ opacity: 1, y: 0, transition: { duration: 600 } }"
  class="overflow-hidden rounded-xl shadow-lg mt-6 border border-gray-200 dark:border-slate-700">
  <table class="w-full text-sm text-left">
    <thead class="bg-gradient-to-r from-blue-700 to-indigo-800 text-white font-bold">
      <tr>
        <th class="px-4 py-3 border-b border-indigo-500 text-center">Isu Aktual</th>
        <th class="px-2 py-3 border-b border-indigo-500 text-center">U</th>
        <th class="px-2 py-3 border-b border-indigo-500 text-center">S</th>
        <th class="px-2 py-3 border-b border-indigo-500 text-center">G</th>
        <th class="px-2 py-3 border-b border-indigo-500 text-center">Total</th>
        <th class="px-3 py-3 border-b border-indigo-500 text-center">Prioritas</th>
      </tr>
    </thead>
    <tbody class="bg-white dark:bg-slate-900 border-b dark:border-slate-700">
      <tr class="hover:bg-blue-50 dark:hover:bg-slate-800 transition-colors border-b dark:border-slate-700 dark:text-gray-200">
        <td class="px-4 py-3">Pengelolaan TA/Skripsi Mahasiswa</td>
        <td class="px-2 py-3 text-center">4</td>
        <td class="px-2 py-3 text-center">4</td>
        <td class="px-2 py-3 text-center">3</td>
        <td class="px-2 py-3 text-center font-bold">11</td>
        <td class="px-3 py-3 text-center">II</td>
      </tr>
      <tr class="bg-blue-100/50 dark:bg-blue-900/30 border-b dark:border-slate-700 font-semibold dark:text-gray-100">
        <td class="px-4 py-3 text-blue-900 dark:text-blue-300 border-l-4 border-blue-600">Data Riset & Pengabdian Dosen Tidak Terpusat</td>
        <td class="px-2 py-3 text-center text-blue-800 dark:text-blue-400">5</td>
        <td class="px-2 py-3 text-center text-blue-800 dark:text-blue-400">5</td>
        <td class="px-2 py-3 text-center text-blue-800 dark:text-blue-400">4</td>
        <td class="px-2 py-3 text-center text-blue-900 dark:text-blue-300 font-bold text-base">14</td>
        <td class="px-3 py-3 align-middle"><div class="text-white bg-blue-600 rounded-full w-8 h-8 flex items-center justify-center mx-auto shadow-md">I</div></td>
      </tr>
      <tr class="hover:bg-blue-50 dark:hover:bg-slate-800 transition-colors dark:text-gray-200">
        <td class="px-4 py-3">Umpan Balik Kepuasan Layanan Digital</td>
        <td class="px-2 py-3 text-center">3</td>
        <td class="px-2 py-3 text-center">3</td>
        <td class="px-2 py-3 text-center">3</td>
        <td class="px-2 py-3 text-center font-bold">9</td>
        <td class="px-3 py-3 text-center">III</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="mt-4 text-sm bg-amber-50 dark:bg-amber-900/20 p-3 rounded-lg border border-amber-200 dark:border-amber-800" v-click>
<b>Alasan Isu #2 Terpilih:</b> U=5 (jadwal akreditasi semakin dekat) · S=5 (memengaruhi nilai akreditasi langsung) · G=4 (volume publikasi terus bertambah tanpa sistem pengelolaan)
</div>

---
layout: default
transition: slide-up
---

# Analisis Akar Masalah — Fishbone

<div v-motion
  :initial="{ opacity: 0, scale: 0.9 }"
  :enter="{ opacity: 1, scale: 1, transition: { duration: 600 } }"
  class="flex justify-center mt-6">
  <img src="./fishbone.png" alt="Fishbone Diagram" class="max-w-[80%] max-h-[40vh] object-contain drop-shadow-xl rounded-xl mx-auto" />
</div>

---
layout: default
---

# Tujuan Aktualisasi

<div class="mt-4 space-y-3">
  <div class="flex gap-3 items-start bg-white/80 dark:bg-slate-800/80 p-3 rounded-lg border dark:border-slate-700 shadow-sm" v-click>
    <div class="bg-blue-600 text-white rounded-full w-8 h-8 flex items-center justify-center flex-shrink-0 font-bold text-sm shadow-md">1</div>
    <p class="text-sm mt-1">Mengimplementasikan pemahaman profil <b>Smart ASN</b> dan <b>Manajemen ASN</b>, serta mendemonstrasikan nilai-nilai dasar <b>BerAKHLAK</b> secara nyata.</p>
  </div>
  <div class="flex gap-3 items-start bg-white/80 dark:bg-slate-800/80 p-3 rounded-lg border dark:border-slate-700 shadow-sm" v-click>
    <div class="bg-blue-600 text-white rounded-full w-8 h-8 flex items-center justify-center flex-shrink-0 font-bold text-sm shadow-md">2</div>
    <p class="text-sm mt-1">Menganalisis akar masalah belum terpusatnya agregasi data riset dosen FSTI ITK menggunakan pisau analisis isu, serta merumuskan gagasan kreatif yang komprehensif.</p>
  </div>
  <div class="flex gap-3 items-start bg-white/80 dark:bg-slate-800/80 p-3 rounded-lg border dark:border-slate-700 shadow-sm" v-click>
    <div class="bg-blue-600 text-white rounded-full w-8 h-8 flex items-center justify-center flex-shrink-0 font-bold text-sm shadow-md">3</div>
    <p class="text-sm mt-1">Membangun prototipe sistem dashboard analitik <b>SINTA Intel</b> dari tahap akuisisi data hingga visualisasi analitik sebagai landasan awal ekosistem di FSTI ITK.</p>
  </div>
</div>

---
layout: default
---

# Manfaat & Ruang Lingkup

<div class="grid grid-cols-2 gap-4 mt-4">
  <div v-motion :initial="{ y: 30, opacity: 0 }" :enter="{ y: 0, opacity: 1, transition: { delay: 100 } }" class="bg-white/90 dark:bg-slate-800/90 p-4 border-t-4 border-blue-500 rounded-lg shadow-md">
    <h3 class="font-bold text-blue-700 dark:text-blue-400 mb-2 text-sm"><i class="fas fa-user-tie mr-1"></i> ASN Dosen</h3>
    <p class="text-xs text-gray-700 dark:text-gray-300">Mengembangkan kompetensi teknis (Python, ML, Vue.js) & mengaktualisasikan BerAKHLAK secara nyata sebagai Smart ASN</p>
  </div>
  <div v-motion :initial="{ y: 30, opacity: 0 }" :enter="{ y: 0, opacity: 1, transition: { delay: 200 } }" class="bg-white/90 dark:bg-slate-800/90 p-4 border-t-4 border-amber-500 rounded-lg shadow-md">
    <h3 class="font-bold text-amber-700 dark:text-amber-400 mb-2 text-sm"><i class="fas fa-building-columns mr-1"></i> Unit Kerja</h3>
    <p class="text-xs text-gray-700 dark:text-gray-300">Tersedia sistem terpusat; keputusan pimpinan berbasis data akurat; persiapan akreditasi program studi lebih mudah</p>
  </div>
  <div v-motion :initial="{ y: 30, opacity: 0 }" :enter="{ y: 0, opacity: 1, transition: { delay: 300 } }" class="bg-white/90 dark:bg-slate-800/90 p-4 border-t-4 border-green-500 rounded-lg shadow-md">
    <h3 class="font-bold text-green-700 dark:text-emerald-400 mb-2 text-sm"><i class="fas fa-landmark mr-1"></i> Institusi (ITK)</h3>
    <p class="text-xs text-gray-700 dark:text-gray-300">Akuntabilitas kinerja terbukti; potensi model <i>best practice</i> yang dapat direplikasi ke prodi lain</p>
  </div>
  <div v-motion :initial="{ y: 30, opacity: 0 }" :enter="{ y: 0, opacity: 1, transition: { delay: 400 } }" class="bg-white/90 dark:bg-slate-800/90 p-4 border-t-4 border-red-500 rounded-lg shadow-md">
    <h3 class="font-bold text-red-700 dark:text-red-400 mb-2 text-sm"><i class="fas fa-earth-asia mr-1"></i> Ekosistem</h3>
    <p class="text-xs text-gray-700 dark:text-gray-300">Terdeteksi peluang kolaborasi riset lintas prodi; terbentuk peta riset ITK; produktivitas meningkat kolektif</p>
  </div>
</div>

<div class="mt-4 bg-purple-50 dark:bg-purple-900/20 p-3 rounded-lg border border-purple-200 dark:border-purple-800 text-sm" v-click>
  <b class="text-purple-700 dark:text-purple-400"><i class="fas fa-expand-arrows-alt mr-1"></i> Batasan:</b>
  <span class="text-gray-700 dark:text-gray-300 block text-xs mt-1">1. Dosen aktif Prodi SI & Bisdig; belum mencakup prodi lain<br>2. Sumber data terbatas API SINTA terbuka & BIMA<br>3. Evaluasi internal; belum mencakup pengujian keamanan eksternal</span>
</div>

---
layout: default
---

# Kondisi Sebelum & Sesudah SINTA Intel

<div class="flex justify-center mt-4">
  <img src="./kondisisebelumsesudah.png" alt="Kondisi Sebelum dan Sesudah SINTA Intel" class="max-h-[70vh] object-contain drop-shadow-xl rounded-xl" />
</div>

---
layout: default
---

# 7 Fitur Utama SINTA Intel

<div class="grid grid-cols-4 gap-2 mt-4">
  <div class="bg-white/90 dark:bg-slate-800/90 p-3 rounded-lg border dark:border-slate-700 shadow-sm" v-click>
    <div class="text-blue-600 text-lg mb-1"><i class="fas fa-chart-line"></i></div>
    <div class="font-bold text-xs text-blue-900 dark:text-blue-300">F1 · Dashboard SINTA</div>
    <p class="text-[10px] text-gray-500 mt-1">Visualisasi metrik Tridharma: publikasi, penelitian, pengabdian, HKI, H-Index per dosen</p>
  </div>
  <div class="bg-white/90 dark:bg-slate-800/90 p-3 rounded-lg border dark:border-slate-700 shadow-sm" v-click>
    <div class="text-teal-600 text-lg mb-1"><i class="fas fa-folder-open"></i></div>
    <div class="font-bold text-xs text-teal-900 dark:text-teal-300">F2 · Research Gallery</div>
    <p class="text-[10px] text-gray-500 mt-1">Galeri 6 kategori karya: publikasi, penelitian, pengabdian, buku, HKI, lainnya</p>
  </div>
  <div class="bg-white/90 dark:bg-slate-800/90 p-3 rounded-lg border dark:border-slate-700 shadow-sm" v-click>
    <div class="text-purple-600 text-lg mb-1"><i class="fas fa-robot"></i></div>
    <div class="font-bold text-xs text-purple-900 dark:text-purple-300">F3 · AI Clustering</div>
    <p class="text-[10px] text-gray-500 mt-1">ML: TF-IDF + K-Means untuk deteksi topik & potensi kolaborasi riset lintas prodi</p>
  </div>
  <div class="bg-white/90 dark:bg-slate-800/90 p-3 rounded-lg border dark:border-slate-700 shadow-sm" v-click>
    <div class="text-orange-600 text-lg mb-1"><i class="fas fa-arrow-trend-up"></i></div>
    <div class="font-bold text-xs text-orange-900 dark:text-orange-300">F4 · Sankey Timeline</div>
    <p class="text-[10px] text-gray-500 mt-1">Evolusi topik riset 2018–sekarang dalam alur visual interaktif</p>
  </div>
</div>

<div class="grid grid-cols-3 gap-2 mt-2">
  <div class="bg-white/90 dark:bg-slate-800/90 p-3 rounded-lg border dark:border-slate-700 shadow-sm" v-click>
    <div class="text-green-600 text-lg mb-1"><i class="fas fa-sack-dollar"></i></div>
    <div class="font-bold text-xs text-green-900 dark:text-green-300">F5 · Funding Dashboard</div>
    <p class="text-[10px] text-gray-500 mt-1">Monitoring aliran dana riset & hibah per dosen; sumber pendanaan internal dan BIMA</p>
  </div>
  <div class="bg-white/90 dark:bg-slate-800/90 p-3 rounded-lg border dark:border-slate-700 shadow-sm" v-click>
    <div class="text-red-600 text-lg mb-1"><i class="fas fa-graduation-cap"></i></div>
    <div class="font-bold text-xs text-red-900 dark:text-red-300">F6 · DTPS Akreditasi</div>
    <p class="text-[10px] text-gray-500 mt-1">Kalkulasi otomatis Rasio Penelitian/DTPS, Pengabdian/DTPS, Dana/DTPS sesuai LKPS standard borang</p>
  </div>
  <div class="bg-white/90 dark:bg-slate-800/90 p-3 rounded-lg border dark:border-slate-700 shadow-sm" v-click>
    <div class="text-amber-600 text-lg mb-1"><i class="fas fa-magnifying-glass"></i></div>
    <div class="font-bold text-xs text-amber-900 dark:text-amber-300">F7 · Expertise Finder</div>
    <p class="text-[10px] text-gray-500 mt-1">Matchmaking pakar berbasis TF-IDF Scoring untuk mitra riset & pengabdian</p>
  </div>
</div>

---
layout: default
---

# 5 Kegiatan Aktualisasi

Setiap kegiatan dilandasi nilai **BerAKHLAK** dan keterkaitan **Smart ASN & Manajemen ASN**:

<br>

<v-clicks>

1. **Pemetaan & Pengumpulan Data Dosen** *(Minggu 1–2)*
   <div class="text-xs text-gray-500 ml-6 mb-3">Inventarisasi data dosen SI & Bisdig dari SINTA · Koordinasi dengan Kaprodi & Wakil Dekan Akademik</div>

2. **Pengembangan Pipeline Scraper Otomatis** *(Minggu 2–3)*
   <div class="text-xs text-gray-500 ml-6 mb-3">Membangun scraper Python yang mengambil data dari SINTA API secara otomatis & terjadwal</div>

3. **Implementasi Fitur Analytics & Dashboard AI** *(Minggu 3–5)*
   <div class="text-xs text-gray-500 ml-6 mb-3">AI Clustering (TF-IDF + K-Means), Sankey Timeline, Research Gallery, Expertise Finder</div>

4. **Implementasi Dashboard Akreditasi & Funding** *(Minggu 4–6)*
   <div class="text-xs text-gray-500 ml-6 mb-3">Fitur DTPS Akreditasi (standar borang prodi) dan Funding Dashboard (monitoring hibah BIMA)</div>

5. **Deployment, Sosialisasi & Evaluasi Sistem** *(Minggu 6–7)*
   <div class="text-xs text-gray-500 ml-6">Deploy ke server ITK · Pelatihan pengguna · Evaluasi & dokumentasi</div>

</v-clicks>

---
layout: default
---

# Kegiatan 1–2: Data & Pipeline

<div class="grid grid-cols-2 gap-4 mt-4">
  <div class="bg-white/90 dark:bg-slate-800/90 p-4 rounded-xl shadow-md border-l-4 border-blue-500">
    <h3 class="font-bold text-blue-700 dark:text-blue-400 text-sm mb-3"><i class="fas fa-database mr-2"></i>Kegiatan 1: Pemetaan Data</h3>
    <div class="text-xs space-y-2 text-gray-700 dark:text-gray-300">
      <div><b>Tahapan:</b></div>
      <ul class="list-disc ml-4 space-y-1">
        <li>Inventarisasi data dosen dari SINTA per prodi</li>
        <li>Koordinasi kebutuhan data dengan pimpinan</li>
        <li>Validasi kelengkapan profil dosen</li>
      </ul>
      <div class="mt-2 bg-blue-50 dark:bg-blue-900/30 p-2 rounded text-[10px]">
        <b>Output:</b> Dokumen inventarisasi data dosen (2 prodi)
      </div>
    </div>
  </div>
  
  <div class="bg-white/90 dark:bg-slate-800/90 p-4 rounded-xl shadow-md border-l-4 border-indigo-500">
    <h3 class="font-bold text-indigo-700 dark:text-indigo-400 text-sm mb-3"><i class="fas fa-code mr-2"></i>Kegiatan 2: Pipeline Scraper</h3>
    <div class="text-xs space-y-2 text-gray-700 dark:text-gray-300">
      <div><b>Tahapan:</b></div>
      <ul class="list-disc ml-4 space-y-1">
        <li>Develop scraper Python (SINTA API)</li>
        <li>Automasi pipeline data berkala</li>
        <li>Data cleaning & normalisasi</li>
      </ul>
      <div class="mt-2 bg-indigo-50 dark:bg-indigo-900/30 p-2 rounded text-[10px]">
        <b>Output:</b> Pipeline scraper otomatis & dataset dosen terstruktur
      </div>
    </div>
  </div>
</div>



---
layout: default
---

# Kegiatan 3: Analytics & Dashboard AI

Inti dari SINTA Intel — implementasi 4 fitur utama berbasis Machine Learning:

<div class="grid grid-cols-2 gap-3 mt-4">
  <div class="bg-purple-50/80 dark:bg-purple-900/20 p-3 rounded-lg border border-purple-200 dark:border-purple-800" v-click>
    <div class="font-bold text-sm text-purple-700 dark:text-purple-400 mb-1"><i class="fas fa-robot mr-1"></i> AI Clustering</div>
    <p class="text-xs text-gray-600 dark:text-gray-400">TF-IDF + K-Means mendeteksi cluster topik riset & potensi kolaborasi lintas prodi secara otomatis</p>
  </div>
  <div class="bg-orange-50/80 dark:bg-orange-900/20 p-3 rounded-lg border border-orange-200 dark:border-orange-800" v-click>
    <div class="font-bold text-sm text-orange-700 dark:text-orange-400 mb-1"><i class="fas fa-arrow-trend-up mr-1"></i> Sankey Timeline</div>
    <p class="text-xs text-gray-600 dark:text-gray-400">Visualisasi evolusi topik riset & pengabdian 2018–sekarang dalam alur interaktif</p>
  </div>
  <div class="bg-teal-50/80 dark:bg-teal-900/20 p-3 rounded-lg border border-teal-200 dark:border-teal-800" v-click>
    <div class="font-bold text-sm text-teal-700 dark:text-teal-400 mb-1"><i class="fas fa-folder-open mr-1"></i> Research Gallery</div>
    <p class="text-xs text-gray-600 dark:text-gray-400">Galeri 6 kategori karya akademik: publikasi, penelitian, pengabdian, buku, HKI, lainnya</p>
  </div>
  <div class="bg-amber-50/80 dark:bg-amber-900/20 p-3 rounded-lg border border-amber-200 dark:border-amber-800" v-click>
    <div class="font-bold text-sm text-amber-700 dark:text-amber-400 mb-1"><i class="fas fa-magnifying-glass mr-1"></i> Expertise Finder</div>
    <p class="text-xs text-gray-600 dark:text-gray-400">Matchmaking pakar berbasis TF-IDF Scoring untuk pelacakan mitra riset & pengabdian</p>
  </div>
</div>

<div class="mt-4 bg-blue-50 dark:bg-blue-900/20 p-3 rounded-lg border border-blue-200 dark:border-blue-800 text-xs" v-click>
  <b class="text-blue-700 dark:text-blue-400">Output:</b> Dashboard analitik berfungsi penuh dengan 4 fitur AI/ML terintegrasi
</div>

---
layout: default
---

# Kegiatan 4–5: Akreditasi & Deployment

<div class="grid grid-cols-2 gap-4 mt-4">
  <div class="bg-white/90 dark:bg-slate-800/90 p-4 rounded-xl shadow-md border-l-4 border-green-500">
    <h3 class="font-bold text-green-700 dark:text-emerald-400 text-sm mb-3"><i class="fas fa-graduation-cap mr-2"></i>Kegiatan 4: Akreditasi & Funding</h3>
    <div class="text-xs space-y-2 text-gray-700 dark:text-gray-300">
      <ul class="list-disc ml-4 space-y-1">
        <li>DTPS Akreditasi: Rasio Penelitian/DTPS, Pengabdian/DTPS, Dana/DTPS otomatis</li>
        <li>Funding Dashboard: aliran hibah BIMA per dosen</li>
        <li>Dashboard SINTA utama + visualisasi metrik</li>
      </ul>
      <div class="mt-2 bg-green-50 dark:bg-green-900/30 p-2 rounded text-[10px]">
        <b>Output:</b> Fitur akreditasi & funding dashboard siap pakai
      </div>
    </div>
  </div>
  
  <div class="bg-white/90 dark:bg-slate-800/90 p-4 rounded-xl shadow-md border-l-4 border-amber-500">
    <h3 class="font-bold text-amber-700 dark:text-amber-400 text-sm mb-3"><i class="fas fa-rocket mr-2"></i>Kegiatan 5: Deploy & Sosialisasi</h3>
    <div class="text-xs space-y-2 text-gray-700 dark:text-gray-300">
      <ul class="list-disc ml-4 space-y-1">
        <li>Deployment ke server ITK</li>
        <li>Pelatihan pengguna (dosen & pimpinan)</li>
        <li>Evaluasi penggunaan & pengumpulan feedback</li>
        <li>Dokumentasi teknis & Manual pengguna</li>
      </ul>
      <div class="mt-2 bg-amber-50 dark:bg-amber-900/30 p-2 rounded text-[10px]">
        <b>Output:</b> Sistem live · Manual pengguna · Laporan evaluasi
      </div>
    </div>
  </div>
</div>

---
layout: image
image: ./matriksberakhlak-kegiatan.png
backgroundSize: contain
class: 'bg-white'
---


---
layout: default
---

# Jadwal Pelaksanaan (7 Minggu)

Pelaksanaan aktualisasi: **7 Maret – 22 April 2026** (Habituasi Off Campus)

<div v-motion
  :initial="{ opacity: 0, scale: 0.95 }"
  :enter="{ opacity: 1, scale: 1, transition: { duration: 700 } }"
  class="mt-4 overflow-hidden rounded-xl shadow-xl border border-gray-200">
  
  <table class="w-full text-xs text-left">
    <thead>
      <tr class="bg-gradient-to-r from-blue-700 to-indigo-800 text-white font-bold text-center">
        <th rowspan="2" class="px-2 py-2 w-8 border border-white/20">No</th>
        <th rowspan="2" class="px-3 py-2 border border-white/20">Kegiatan</th>
        <th colspan="3" class="px-2 py-2 border border-white/20 bg-blue-800/50">Maret 2026</th>
        <th colspan="4" class="px-2 py-2 border border-white/20 bg-teal-700/50">April 2026</th>
      </tr>
      <tr class="bg-slate-800 text-white text-[10px] text-center border-b border-white/20">
        <th class="py-1 w-[8%] border border-white/20">M1<br/>07-13</th>
        <th class="py-1 w-[8%] border border-white/20">M2<br/>14-20</th>
        <th class="py-1 w-[8%] border border-white/20">M3<br/>21-27</th>
        <th class="py-1 w-[8%] border border-white/20">M4<br/>28-03</th>
        <th class="py-1 w-[8%] border border-white/20">M5<br/>04-10</th>
        <th class="py-1 w-[8%] border border-white/20">M6<br/>11-17</th>
        <th class="py-1 w-[8%] border border-white/20">M7<br/>18-22</th>
      </tr>
    </thead>
    <tbody class="bg-gray-50 dark:bg-slate-900 text-center text-gray-800 dark:text-gray-200">
<tr class="border-b border-gray-200 dark:border-slate-700">
<td class="py-2 border-r border-gray-200">1</td>
<td class="px-3 py-2 text-left border-r border-gray-200">Pemetaan & Pengumpulan Data</td>
<td class="bg-blue-500 border border-white"><div class="w-2 h-2 bg-white rounded-full mx-auto"></div></td>
<td class="bg-blue-500 border border-white"><div class="w-2 h-2 bg-white rounded-full mx-auto"></div></td>
<td class="border-r border-gray-200"></td>
<td></td><td></td><td></td><td></td>
</tr>
<tr class="border-b border-gray-200 dark:border-slate-700">
<td class="py-2 border-r border-gray-200">2</td>
<td class="px-3 py-2 text-left border-r border-gray-200">Pipeline Scraper SINTA</td>
<td class="border-r border-gray-200"></td>
<td class="bg-blue-600 border border-white"><div class="w-2 h-2 bg-white rounded-full mx-auto"></div></td>
<td class="bg-blue-600 border border-white"><div class="w-2 h-2 bg-white rounded-full mx-auto"></div></td>
<td></td><td></td><td></td><td></td>
</tr>
<tr class="border-b border-gray-200 dark:border-slate-700">
<td class="py-2 border-r border-gray-200">3</td>
<td class="px-3 py-2 text-left border-r border-gray-200">Analytics & Dashboard AI</td>
<td class="border-r border-gray-200"></td>
<td class="border-r border-gray-200"></td>
<td class="bg-blue-700 border border-white"><div class="w-2 h-2 bg-white rounded-full mx-auto"></div></td>
<td class="bg-blue-700 border border-white"><div class="w-2 h-2 bg-white rounded-full mx-auto"></div></td>
<td class="bg-blue-700 border border-white"><div class="w-2 h-2 bg-white rounded-full mx-auto"></div></td>
<td></td><td></td>
</tr>
<tr class="border-b border-gray-200 dark:border-slate-700">
<td class="py-2 border-r border-gray-200">4</td>
<td class="px-3 py-2 text-left border-r border-gray-200">Dashboard Akreditasi & Funding</td>
<td class="border-r border-gray-200"></td>
<td class="border-r border-gray-200"></td>
<td class="border-r border-gray-200"></td>
<td class="bg-indigo-600 border border-white"><div class="w-2 h-2 bg-white rounded-full mx-auto"></div></td>
<td class="bg-indigo-600 border border-white"><div class="w-2 h-2 bg-white rounded-full mx-auto"></div></td>
<td class="bg-indigo-600 border border-white"><div class="w-2 h-2 bg-white rounded-full mx-auto"></div></td>
<td></td>
</tr>
<tr class="">
<td class="py-2 border-r border-gray-200">5</td>
<td class="px-3 py-2 text-left border-r border-gray-200">Deploy, Sosialisasi & Evaluasi</td>
<td class="border-r border-gray-200"></td>
<td class="border-r border-gray-200"></td>
<td class="border-r border-gray-200"></td>
<td class="border-r border-gray-200"></td>
<td class="border-r border-gray-200"></td>
<td class="bg-indigo-700 border border-white"><div class="w-2 h-2 bg-white rounded-full mx-auto"></div></td>
<td class="bg-indigo-700 border border-white"><div class="w-2 h-2 bg-white rounded-full mx-auto"></div></td>
</tr>
    </tbody>
  </table>
  
  <div class="bg-white dark:bg-slate-800 p-3 text-[10px] text-gray-500 dark:text-gray-400 border-t border-gray-200 flex justify-between">
    <div class="flex items-center gap-2"><div class="w-3 h-3 bg-blue-500 border shadow-sm"></div> = Minggu aktif kegiatan berlangsung</div>
    <div><i>*M1–M3 = Maret 2026 | M4–M7 = April 2026</i></div>
  </div>
</div>

---
layout: default
---

# Rencana Output & Deliverables

<div class="grid grid-cols-2 gap-3 mt-4">
  <div class="bg-white/90 dark:bg-slate-800/90 p-3 rounded-lg border dark:border-slate-700 shadow-sm flex gap-3 items-start" v-click>
    <div class="bg-blue-100 dark:bg-blue-900/50 rounded-lg p-2 text-blue-600"><i class="fas fa-globe text-lg"></i></div>
    <div>
      <div class="font-bold text-xs">Sistem SINTA Intel</div>
      <p class="text-[10px] text-gray-500 mt-1">Dashboard web analitik live di server ITK dengan 7 fitur utama terintegrasi</p>
    </div>
  </div>
  <div class="bg-white/90 dark:bg-slate-800/90 p-3 rounded-lg border dark:border-slate-700 shadow-sm flex gap-3 items-start" v-click>
    <div class="bg-green-100 dark:bg-green-900/50 rounded-lg p-2 text-green-600"><i class="fas fa-database text-lg"></i></div>
    <div>
      <div class="font-bold text-xs">Pipeline Scraper Otomatis</div>
      <p class="text-[10px] text-gray-500 mt-1">Script Python yang mengambil data SINTA secara terjadwal & otomatis</p>
    </div>
  </div>
  <div class="bg-white/90 dark:bg-slate-800/90 p-3 rounded-lg border dark:border-slate-700 shadow-sm flex gap-3 items-start" v-click>
    <div class="bg-purple-100 dark:bg-purple-900/50 rounded-lg p-2 text-purple-600"><i class="fas fa-file-alt text-lg"></i></div>
    <div>
      <div class="font-bold text-xs">Dokumentasi & Manual Pengguna</div>
      <p class="text-[10px] text-gray-500 mt-1">Buku panduan operasional (user guide) dan dokumentasi teknis pengelolaan data riset</p>
    </div>
  </div>
  <div class="bg-white/90 dark:bg-slate-800/90 p-3 rounded-lg border dark:border-slate-700 shadow-sm flex gap-3 items-start" v-click>
    <div class="bg-amber-100 dark:bg-amber-900/50 rounded-lg p-2 text-amber-600"><i class="fas fa-chart-pie text-lg"></i></div>
    <div>
      <div class="font-bold text-xs">Laporan Evaluasi</div>
      <p class="text-[10px] text-gray-500 mt-1">Hasil evaluasi penggunaan, feedback pengguna, dan rekomendasi pengembangan</p>
    </div>
  </div>
</div>

<div class="mt-4 bg-blue-50 dark:bg-blue-900/20 p-3 rounded-lg border border-blue-200 dark:border-blue-800 text-center text-sm" v-click>
  <b>"Transformasi Digital untuk Akuntabilitas Tridharma Perguruan Tinggi"</b>
</div>

---
layout: center
class: text-center
---

# Terima Kasih
**Mohon Arahan dan Masukannya**

<div class="mt-8 text-sm text-gray-500 dark:text-gray-400">
  <p>Aidil Saputra Kirsan, S.ST., M.Tr.Kom</p>
  <p class="text-xs">Dosen Asisten Ahli / Kepala Lab Inovasi Digital</p>
  <p class="text-xs">Prodi Sistem Informasi · FSTI · Institut Teknologi Kalimantan</p>
</div>
