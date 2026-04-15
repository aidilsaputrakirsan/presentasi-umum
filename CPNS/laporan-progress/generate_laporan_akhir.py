"""
Generator Laporan Akhir Aktualisasi SITRIA
Pelatihan Dasar CPNS Angkatan VI Tahun 2026
Institut Teknologi Kalimantan
"""

from docx import Document
from docx.shared import Pt, Cm, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

# ─────────────────────────────────────────────
#  HELPER FUNCTIONS
# ─────────────────────────────────────────────

def set_cell_bg(cell, hex_color):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color)
    tcPr.append(shd)

def set_cell_borders(cell, top=None, bottom=None, left=None, right=None):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    for side, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        if val:
            el = OxmlElement(f'w:{side}')
            el.set(qn('w:val'), val.get('val', 'single'))
            el.set(qn('w:sz'), str(val.get('sz', 4)))
            el.set(qn('w:space'), '0')
            el.set(qn('w:color'), val.get('color', '000000'))
            tcBorders.append(el)
    tcPr.append(tcBorders)

def add_page_break(doc):
    p = doc.add_paragraph()
    run = p.add_run()
    run.add_break(docx_break_type())
    return p

def docx_break_type():
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    br = OxmlElement('w:br')
    br.set(qn('w:type'), 'page')
    return br

def page_break(doc):
    doc.add_page_break()

def heading(doc, text, level=1, color=None, center=False):
    p = doc.add_heading(text, level=level)
    if color:
        for run in p.runs:
            run.font.color.rgb = RGBColor(*bytes.fromhex(color))
    if center:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    return p

def para(doc, text='', bold=False, italic=False, size=11, align=None, space_before=0, space_after=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    if align == 'center':
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    elif align == 'right':
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    elif align == 'justify':
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if text:
        run = p.add_run(text)
        run.bold = bold
        run.italic = italic
        run.font.size = Pt(size)
    return p

def add_run(p, text, bold=False, italic=False, size=11):
    run = p.add_run(text)
    run.bold = bold
    run.italic = italic
    run.font.size = Pt(size)
    return run

def img_placeholder(doc, nomor_gambar, nama_file, keterangan, catatan_ukuran='Screenshot landscape (16:9)'):
    """Placeholder kotak bergaris untuk gambar yang perlu disisipkan manual."""
    table = doc.add_table(rows=2, cols=1)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    # Baris header
    hdr = table.rows[0].cells[0]
    set_cell_bg(hdr, 'D6EAF8')
    ph = hdr.paragraphs[0]
    ph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    ph.paragraph_format.space_before = Pt(3)
    ph.paragraph_format.space_after = Pt(3)
    run = ph.add_run(f'[ SISIPKAN GAMBAR DI SINI ]')
    run.bold = True
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(0x1A, 0x53, 0x76)

    # Baris isi
    body = table.rows[1].cells[0]
    set_cell_bg(body, 'EBF5FB')
    pb = body.paragraphs[0]
    pb.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pb.paragraph_format.space_before = Pt(30)
    pb.paragraph_format.space_after = Pt(30)
    run2 = pb.add_run(f'Nama file  : {nama_file}\nKeterangan : {keterangan}')
    run2.font.size = Pt(10)
    run2.italic = True

    # Caption di bawah
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(2)
    p_cap.paragraph_format.space_after = Pt(10)
    rc = p_cap.add_run(f'Gambar {nomor_gambar}. {keterangan}   ({catatan_ukuran})')
    rc.italic = True
    rc.font.size = Pt(10)


def section_title(doc, text, color='003366'):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text)
    run.bold = True
    run.font.size = Pt(12)
    run.font.color.rgb = RGBColor(*bytes.fromhex(color))
    return p

def add_table_row(table, cells_data, bold_col0=True, bg_header=None, font_size=10):
    row = table.add_row()
    for i, cell_data in enumerate(cells_data):
        cell = row.cells[i]
        cell.text = str(cell_data) if cell_data is not None else ''
        for para in cell.paragraphs:
            para.paragraph_format.space_before = Pt(2)
            para.paragraph_format.space_after = Pt(2)
            for run in para.runs:
                run.font.size = Pt(font_size)
                if i == 0 and bold_col0:
                    run.bold = True
        if bg_header:
            set_cell_bg(cell, bg_header)
    return row

def make_table(doc, headers, col_widths=None):
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_row = table.rows[0]
    for i, h in enumerate(headers):
        cell = hdr_row.cells[i]
        cell.text = h
        set_cell_bg(cell, '003366')
        for para in cell.paragraphs:
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            para.paragraph_format.space_before = Pt(2)
            para.paragraph_format.space_after = Pt(2)
            for run in para.runs:
                run.bold = True
                run.font.color.rgb = RGBColor(255, 255, 255)
                run.font.size = Pt(10)
    if col_widths:
        for i, w in enumerate(col_widths):
            for cell in table.columns[i].cells:
                cell.width = Cm(w)
    return table

def horizontal_line(doc):
    p = doc.add_paragraph()
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '6')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), '003366')
    pBdr.append(bottom)
    pPr.append(pBdr)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(6)
    return p


# ─────────────────────────────────────────────
#  DATA
# ─────────────────────────────────────────────

DATA = {
    'nama': 'Aidil Saputra Kirsan, S.ST., M.Tr.Kom',
    'nip': '199403172025061004',
    'jabatan': 'Dosen Asisten Ahli / Kepala Lab Inovasi Digital',
    'pangkat': 'Penata Muda Tk.I / III-b',
    'unit_kerja': 'Lab Inovasi Digital, Prodi Sistem Informasi, FSTI ITK',
    'instansi': 'Institut Teknologi Kalimantan',
    'alamat': 'Jl. Soekarno-Hatta KM 15, Balikpapan, Kaltim 76127',
    'mentor_nama': 'Irma Fitria, S.Si., M.Si',
    'mentor_nip': '199303232022032016',
    'mentor_jabatan': 'Wakil Dekan Bidang Akademik dan Kemahasiswaan FSTI ITK',
    'coach_nama': 'Mustari Kurniawati, S.IP., MPA',
    'coach_nip': '197712232005012001',
    'penguji_nama': 'Dr. M. Muhamad Harry Rahmadi, S.Pi., MM.',
    'penguji_nip': '198510092011011012',
    'angkatan': 'VI',
    'kelompok': 'I',
    'tahun': '2026',
    'penyelenggara': 'Pusat Pelatihan dan Pengembangan – LAN RI',
    'judul': 'Pengembangan Sistem Dashboard Analitik Tridharma Berbasis Data Multi-Sumber (SITRIA) pada Lab Inovasi Digital FSTI ITK',
    'periode': '7 Maret – 22 April 2026',
    'tanggal_laporan': '15 April 2026',
    'tanggal_seminar': '21 April 2026',
    'tempat_seminar': 'Online / Daring',
}


# ─────────────────────────────────────────────
#  DOCUMENT SETUP
# ─────────────────────────────────────────────

doc = Document()

# Page margins
for section in doc.sections:
    section.top_margin = Cm(3)
    section.bottom_margin = Cm(2.5)
    section.left_margin = Cm(4)
    section.right_margin = Cm(3)

# Default paragraph style
style = doc.styles['Normal']
style.font.name = 'Times New Roman'
style.font.size = Pt(12)


# ═══════════════════════════════════════════════
#  1. HALAMAN SAMPUL
# ═══════════════════════════════════════════════

p = para(doc, 'LAPORAN AKTUALISASI', bold=True, size=16, align='center', space_before=20, space_after=4)
p = para(doc, 'PELATIHAN DASAR CPNS ANGKATAN VI TAHUN 2026', bold=True, size=13, align='center', space_after=4)
p = para(doc, 'PUSAT PELATIHAN DAN PENGEMBANGAN – LAN RI', bold=False, size=11, align='center', space_after=20)

horizontal_line(doc)

p = para(doc, '', space_before=10, space_after=4)
p = para(doc, 'SITRIA', bold=True, size=22, align='center', space_after=2)
p = para(doc, 'Sistem Informasi Tridharma Akademik', bold=True, size=14, align='center', space_after=4)
p = para(doc, 'Dashboard Analitik Tridharma Dosen Berbasis Data Multi-Sumber', italic=True, size=11, align='center', space_after=2)
p = para(doc, 'Lab Inovasi Digital – Prodi Sistem Informasi & Bisnis Digital', italic=True, size=10, align='center', space_after=2)
p = para(doc, 'Fakultas Sains dan Teknologi Industri – Institut Teknologi Kalimantan', italic=True, size=10, align='center', space_after=20)

horizontal_line(doc)

p = para(doc, 'Disusun oleh:', size=11, align='center', space_before=10, space_after=4)
p = para(doc, DATA['nama'], bold=True, size=13, align='center', space_after=2)
p = para(doc, f"NIP. {DATA['nip']}", size=11, align='center', space_after=2)
p = para(doc, DATA['jabatan'], size=11, align='center', space_after=2)
p = para(doc, DATA['unit_kerja'], size=11, align='center', space_after=20)

horizontal_line(doc)

p = para(doc, f"Periode Aktualisasi: {DATA['periode']}", size=11, align='center', space_before=8, space_after=2)
p = para(doc, f"Tanggal Laporan: {DATA['tanggal_laporan']}", size=11, align='center', space_after=20)

page_break(doc)


# ═══════════════════════════════════════════════
#  2. LEMBAR PERNYATAAN ORISINALITAS
# ═══════════════════════════════════════════════

heading(doc, 'LEMBAR PERNYATAAN ORISINALITAS LAPORAN AKTUALISASI', level=1, center=True)
horizontal_line(doc)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.paragraph_format.space_after = Pt(10)
add_run(p, 'Saya yang bertanda tangan di bawah ini:', size=12)

# Identitas tabel
table = doc.add_table(rows=5, cols=3)
table.style = 'Table Grid'
rows_data = [
    ('Nama', ':', DATA['nama']),
    ('NIP', ':', DATA['nip']),
    ('Jabatan', ':', DATA['jabatan']),
    ('Unit Kerja', ':', DATA['unit_kerja']),
    ('Instansi', ':', DATA['instansi']),
]
for i, (k, sep, v) in enumerate(rows_data):
    row = table.rows[i]
    row.cells[0].text = k
    row.cells[1].text = sep
    row.cells[2].text = v
    row.cells[0].width = Cm(4)
    row.cells[1].width = Cm(0.5)
    for cell in row.cells:
        for par in cell.paragraphs:
            for run in par.runs:
                run.font.size = Pt(11)
            par.paragraph_format.space_before = Pt(2)
            par.paragraph_format.space_after = Pt(2)
    row.cells[0].paragraphs[0].runs[0].bold = True

doc.add_paragraph()

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.paragraph_format.space_after = Pt(8)
add_run(p, 'Menyatakan bahwa Laporan Aktualisasi yang berjudul ', size=12)
add_run(p, f'"{DATA["judul"]}"', bold=True, size=12)
add_run(p, ' ini adalah hasil karya saya sendiri dan bebas dari plagiarisme. '
           'Kutipan dan referensi yang digunakan telah dicantumkan dengan benar dan sesuai ketentuan yang berlaku. '
           'Apabila terbukti pernyataan ini tidak benar, maka saya bersedia menerima sanksi sesuai peraturan yang berlaku.', size=12)

p = para(doc, f'Balikpapan, {DATA["tanggal_laporan"]}', size=12, align='right', space_before=20, space_after=2)
p = para(doc, 'Yang Menyatakan,', size=12, align='right', space_after=60)
p = para(doc, DATA['nama'], bold=True, size=12, align='right', space_after=2)
p = para(doc, f"NIP. {DATA['nip']}", size=12, align='right')

page_break(doc)


# ═══════════════════════════════════════════════
#  3. LEMBAR PERSETUJUAN
# ═══════════════════════════════════════════════

heading(doc, 'LEMBAR PERSETUJUAN LAPORAN AKTUALISASI', level=1, center=True)
horizontal_line(doc)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
add_run(p, 'Laporan Aktualisasi ini diajukan oleh:', size=12)

table = doc.add_table(rows=5, cols=3)
table.style = 'Table Grid'
rows_data = [
    ('Nama', ':', DATA['nama']),
    ('NIP', ':', DATA['nip']),
    ('Jabatan', ':', DATA['jabatan']),
    ('Unit Kerja', ':', DATA['unit_kerja']),
    ('Judul', ':', DATA['judul']),
]
for i, (k, sep, v) in enumerate(rows_data):
    row = table.rows[i]
    row.cells[0].text = k
    row.cells[1].text = sep
    row.cells[2].text = v
    row.cells[0].width = Cm(4)
    row.cells[1].width = Cm(0.5)
    for cell in row.cells:
        for par in cell.paragraphs:
            for run in par.runs:
                run.font.size = Pt(11)
            par.paragraph_format.space_before = Pt(2)
            par.paragraph_format.space_after = Pt(2)
    row.cells[0].paragraphs[0].runs[0].bold = True

doc.add_paragraph()
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
add_run(p, 'Telah mendapat persetujuan untuk diseminarkan sebagai Laporan Aktualisasi '
           f'Pelatihan Dasar CPNS Angkatan {DATA["angkatan"]} Tahun {DATA["tahun"]}.', size=12)

p = para(doc, f'Balikpapan, {DATA["tanggal_laporan"]}', size=12, space_before=20, space_after=4)

# TTD grid
table_ttd = doc.add_table(rows=1, cols=2)
table_ttd.alignment = WD_TABLE_ALIGNMENT.CENTER
cells_ttd = table_ttd.rows[0].cells
for i, (role, nama, nip) in enumerate([
    ('Menyetujui, Coach', DATA['coach_nama'], f"NIP. {DATA['coach_nip']}"),
    ('Mengetahui, Mentor', DATA['mentor_nama'], f"NIP. {DATA['mentor_nip']}"),
]):
    c = cells_ttd[i]
    c.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_run(c.paragraphs[0], role, size=11)
    p2 = c.add_paragraph('\n\n\n')
    p3 = c.add_paragraph(nama)
    p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p3.runs[0].bold = True
    p3.runs[0].font.size = Pt(11)
    p4 = c.add_paragraph(nip)
    p4.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p4.runs[0].font.size = Pt(11)

page_break(doc)


# ═══════════════════════════════════════════════
#  4. LEMBAR PENGESAHAN
# ═══════════════════════════════════════════════

heading(doc, 'LEMBAR PENGESAHAN LAPORAN AKTUALISASI', level=1, center=True)
horizontal_line(doc)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
add_run(p, 'Laporan Aktualisasi ini telah diseminarkan di hadapan penguji dan dinyatakan '
           'telah memenuhi syarat untuk diterima.', size=12)

table = doc.add_table(rows=6, cols=3)
table.style = 'Table Grid'
rows_data = [
    ('Nama', ':', DATA['nama']),
    ('NIP', ':', DATA['nip']),
    ('Jabatan', ':', DATA['jabatan']),
    ('Unit Kerja', ':', DATA['unit_kerja']),
    ('Tanggal Seminar', ':', DATA['tanggal_seminar']),
    ('Tempat', ':', DATA['tempat_seminar']),
]
for i, (k, sep, v) in enumerate(rows_data):
    row = table.rows[i]
    row.cells[0].text = k
    row.cells[1].text = sep
    row.cells[2].text = v
    row.cells[0].width = Cm(4.5)
    row.cells[1].width = Cm(0.5)
    for cell in row.cells:
        for par in cell.paragraphs:
            for run in par.runs:
                run.font.size = Pt(11)
            par.paragraph_format.space_before = Pt(2)
            par.paragraph_format.space_after = Pt(2)
    row.cells[0].paragraphs[0].runs[0].bold = True

doc.add_paragraph()

table_ttd = doc.add_table(rows=1, cols=3)
table_ttd.alignment = WD_TABLE_ALIGNMENT.CENTER
for i, (role, nama, nip) in enumerate([
    ('Penguji', DATA['penguji_nama'], f"NIP. {DATA['penguji_nip']}"),
    ('Coach', DATA['coach_nama'], f"NIP. {DATA['coach_nip']}"),
    ('Mentor', DATA['mentor_nama'], f"NIP. {DATA['mentor_nip']}"),
]):
    c = table_ttd.rows[0].cells[i]
    c.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_run(c.paragraphs[0], role, bold=True, size=11)
    p2 = c.add_paragraph('\n\n\n')
    p3 = c.add_paragraph(nama)
    p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p3.runs[0].bold = True
    p3.runs[0].font.size = Pt(10)
    p4 = c.add_paragraph(nip)
    p4.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p4.runs[0].font.size = Pt(10)

page_break(doc)


# ═══════════════════════════════════════════════
#  5. LEMBAR KONSULTASI MENTOR
# ═══════════════════════════════════════════════

heading(doc, 'LEMBAR KONSULTASI MENTOR', level=1, center=True)
horizontal_line(doc)

p = doc.add_paragraph()
add_run(p, 'Nama Mentor\t: ', bold=True, size=11)
add_run(p, DATA['mentor_nama'], size=11)
p2 = doc.add_paragraph()
add_run(p2, 'NIP\t\t\t: ', bold=True, size=11)
add_run(p2, DATA['mentor_nip'], size=11)
p3 = doc.add_paragraph()
add_run(p3, 'Jabatan\t\t: ', bold=True, size=11)
add_run(p3, DATA['mentor_jabatan'], size=11)
doc.add_paragraph()

tbl = make_table(doc,
    ['No', 'Tanggal', 'Uraian Konsultasi / Catatan', 'Paraf Mentor'],
    col_widths=[1, 3, 9, 3])

konsultasi_mentor = [
    ('1', '____________ 2026', 'Konsultasi persetujuan rancangan aktualisasi dan dukungan pimpinan unit kerja', ''),
    ('2', '____________ 2026', 'Penyelarasan gagasan "SITRIA" dan batasan sasaran dashboard', ''),
    ('3', '____________ 2026', 'Review progres Kegiatan 1 dan 2: data dosen dan pipeline scraper SINTA', ''),
    ('4', '____________ 2026', 'Review progres Kegiatan 3 dan 4: fitur analitik dan dashboard akreditasi', ''),
    ('5', '____________ 2026', 'Konsultasi final laporan aktualisasi dan persiapan seminar', ''),
]
for row_data in konsultasi_mentor:
    r = tbl.add_row()
    for i, val in enumerate(row_data):
        r.cells[i].text = val
        r.cells[i].paragraphs[0].paragraph_format.space_before = Pt(2)
        r.cells[i].paragraphs[0].paragraph_format.space_after = Pt(2)
        for run in r.cells[i].paragraphs[0].runs:
            run.font.size = Pt(10)
        if i == 0:
            r.cells[i].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER

page_break(doc)


# ═══════════════════════════════════════════════
#  6. LEMBAR KONSULTASI COACH
# ═══════════════════════════════════════════════

heading(doc, 'LEMBAR KONSULTASI COACH', level=1, center=True)
horizontal_line(doc)

p = doc.add_paragraph()
add_run(p, 'Nama Coach\t: ', bold=True, size=11)
add_run(p, DATA['coach_nama'], size=11)
p2 = doc.add_paragraph()
add_run(p2, 'NIP\t\t\t: ', bold=True, size=11)
add_run(p2, DATA['coach_nip'], size=11)
doc.add_paragraph()

tbl = make_table(doc,
    ['No', 'Tanggal', 'Uraian Konsultasi / Catatan', 'Paraf Coach'],
    col_widths=[1, 3, 9, 3])

konsultasi_coach = [
    ('1', '____________ 2026', 'Konsultasi awal: pemaparan rancangan dan gagasan kreatif SITRIA', ''),
    ('2', '____________ 2026', 'Review usulan kegiatan kritis pemecahan masalah (gagasan kreatif "SITRIA")', ''),
    ('3', '____________ 2026', 'Penguatan relevansi nilai BerAKHLAK pada setiap kegiatan aktualisasi', ''),
    ('4', '____________ 2026', 'Review implementasi Kegiatan 3–5 dan bukti-bukti pendukung', ''),
    ('5', '____________ 2026', 'Konsultasi penyusunan laporan akhir dan persiapan seminar aktualisasi', ''),
]
for row_data in konsultasi_coach:
    r = tbl.add_row()
    for i, val in enumerate(row_data):
        r.cells[i].text = val
        r.cells[i].paragraphs[0].paragraph_format.space_before = Pt(2)
        r.cells[i].paragraphs[0].paragraph_format.space_after = Pt(2)
        for run in r.cells[i].paragraphs[0].runs:
            run.font.size = Pt(10)
        if i == 0:
            r.cells[i].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER

page_break(doc)


# ═══════════════════════════════════════════════
#  7. OPR — ONE PAGE REPORT
# ═══════════════════════════════════════════════

heading(doc, 'OPR — ONE PAGE REPORT', level=1, center=True)
horizontal_line(doc)

opr_table = doc.add_table(rows=0, cols=2)
opr_table.style = 'Table Grid'
opr_table.alignment = WD_TABLE_ALIGNMENT.CENTER

def opr_row(table, label, value):
    row = table.add_row()
    row.cells[0].text = label
    row.cells[0].width = Cm(5.5)
    row.cells[1].text = value
    for par in row.cells[0].paragraphs:
        par.runs[0].bold = True
        par.runs[0].font.size = Pt(10)
        par.paragraph_format.space_before = Pt(2)
        par.paragraph_format.space_after = Pt(2)
    for par in row.cells[1].paragraphs:
        for run in par.runs:
            run.font.size = Pt(10)
        par.paragraph_format.space_before = Pt(2)
        par.paragraph_format.space_after = Pt(2)
        par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

opr_row(opr_table, 'Nama Peserta', DATA['nama'])
opr_row(opr_table, 'NIP', DATA['nip'])
opr_row(opr_table, 'Jabatan', DATA['jabatan'])
opr_row(opr_table, 'Unit Kerja', DATA['unit_kerja'])
opr_row(opr_table, 'Instansi', DATA['instansi'])
opr_row(opr_table, 'Angkatan/Kelompok', f"Angkatan {DATA['angkatan']} / Kelompok {DATA['kelompok']}")
opr_row(opr_table, 'Mentor', DATA['mentor_nama'])
opr_row(opr_table, 'Coach', DATA['coach_nama'])
opr_row(opr_table, 'Judul Aktualisasi', DATA['judul'])
opr_row(opr_table, 'Isu Terpilih',
        'Pengelolaan Data Riset dan Pengabdian Dosen di Lab Inovasi Digital Belum Terpusat dan Teranalisis '
        '(Skor USG: 14 — Urgency=5, Seriousness=5, Growth=4)')
opr_row(opr_table, 'Gagasan Kreatif',
        'SITRIA (Sistem Informasi Tridharma Akademik): Dashboard analitik berbasis web yang mengintegrasikan data '
        'riset, publikasi, dan pengabdian dosen secara otomatis dari portal SINTA Kemdiktisaintek menggunakan '
        'Python, AI/ML (TF-IDF + K-Means), dan Vue.js.')
opr_row(opr_table, 'Kegiatan Utama (5)',
        '1. Pemetaan & Pengumpulan Data Dosen (07–20 Mar)\n'
        '2. Pengembangan Pipeline Scraper SINTA Otomatis (14–27 Mar)\n'
        '3. Implementasi Fitur Analitik & Dashboard (21 Mar – 10 Apr)\n'
        '4. Dashboard Akreditasi DTPS & Pendanaan Riset (28 Mar – 17 Apr)\n'
        '5. Peluncuran, Sosialisasi & Evaluasi SITRIA (11–22 Apr)')
opr_row(opr_table, 'Output Utama',
        '• 25 dosen terdata dari 2 prodi (SI & Bisnis Digital)\n'
        '• 7 fitur dashboard aktif: Analitik Utama, Research Gallery, AI Clustering, Sankey Timeline, '
        'Funding Dashboard, DTPS Akreditasi, Expertise Finder\n'
        '• Sistem diluncurkan ke server Lab Inovasi Digital, 15 April 2026\n'
        '• 23 peserta sosialisasi dari kalangan dosen, Kaprodi, dan laboran')
opr_row(opr_table, 'Nilai BerAKHLAK',
        'Berorientasi Pelayanan (data real-time bagi pimpinan), Akuntabel (kalkulasi DTPS otomatis), '
        'Kompeten (Python, ML, Vue.js), Harmonis (kolaborasi lintas prodi), Loyal (mendukung akreditasi ITK), '
        'Adaptif (data multi-sumber, AI/ML), Kolaboratif (melibatkan semua pemangku kepentingan)')
opr_row(opr_table, 'Manfaat Utama',
        '• Bagi Prodi SI & Bisnis Digital: persiapan borang akreditasi lebih cepat dan akurat\n'
        '• Bagi pimpinan FSTI: monitoring kinerja Tridharma dosen secara real-time\n'
        '• Bagi dosen: visibilitas profil riset dan deteksi peluang kolaborasi\n'
        '• Bagi institusi: model best practice yang berpotensi direplikasi ke prodi lain')
opr_row(opr_table, 'Status Penyelesaian',
        'SELESAI 100% — Semua 5 kegiatan dan 25 tahapan aktualisasi berhasil diselesaikan dalam periode 7 Maret – 22 April 2026')

page_break(doc)


# ═══════════════════════════════════════════════
#  8. KATA PENGANTAR
# ═══════════════════════════════════════════════

heading(doc, 'KATA PENGANTAR', level=1, center=True)
horizontal_line(doc)

kata_pengantar_paras = [
    ('Puji syukur penulis panjatkan kepada Tuhan Yang Maha Esa atas limpahan rahmat dan karunia-Nya '
     'sehingga penulis dapat menyelesaikan penyusunan Laporan Aktualisasi ini dalam rangka '
     'Pelatihan Dasar CPNS Angkatan VI Tahun 2026 Institut Teknologi Kalimantan.'),
    ('Laporan Aktualisasi berjudul "Pengembangan Sistem Dashboard Analitik Tridharma Berbasis Data '
     'Multi-Sumber (SITRIA) pada Lab Inovasi Digital FSTI Institut Teknologi Kalimantan" ini disusun '
     'sebagai wujud internalisasi dan implementasi nilai-nilai dasar ASN BerAKHLAK serta peran dan '
     'kedudukan PNS dalam mendukung terwujudnya tata kelola pemerintahan yang cerdas.'),
    ('Laporan ini merupakan dokumentasi pelaksanaan seluruh kegiatan aktualisasi selama periode habituasi '
     '7 Maret – 22 April 2026 di Lab Inovasi Digital, Prodi Sistem Informasi, FSTI ITK. Seluruh '
     'rangkaian kegiatan mulai dari pemetaan data dosen, pengembangan sistem pengambilan data otomatis, '
     'implementasi dashboard analitik, hingga peluncuran dan sosialisasi sistem telah berhasil diselesaikan '
     'sesuai rencana yang telah ditetapkan.'),
    ('Penulis mengucapkan terima kasih kepada: (1) Rektor ITK atas kesempatan mengikuti Latsar CPNS; '
     '(2) Ibu Mustari Kurniawati, S.IP., MPA selaku Coach atas bimbingan dan arahan yang diberikan; '
     '(3) Ibu Irma Fitria, S.Si., M.Si selaku Mentor atas dukungan penuh dari lingkungan unit kerja; '
     '(4) Pimpinan FSTI ITK atas dukungan institusional; (5) Koordinator Prodi Sistem Informasi dan '
     'Prodi Bisnis Digital atas kerja sama dalam validasi data dan sosialisasi sistem; '
     '(6) Seluruh rekan peserta Latsar CPNS Angkatan VI Tahun 2026.'),
    ('Semoga Laporan Aktualisasi ini dapat memberikan manfaat nyata bagi peningkatan kinerja dan '
     'kualitas layanan Lab Inovasi Digital, Program Studi Sistem Informasi, dan Program Studi Bisnis '
     'Digital FSTI ITK, serta menjadi kontribusi positif bagi pengembangan tata kelola akademik '
     'Institut Teknologi Kalimantan.'),
]

for text in kata_pengantar_paras:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.first_line_indent = Cm(1.25)
    add_run(p, text, size=12)

p = para(doc, f'Balikpapan, {DATA["tanggal_laporan"]}', size=12, align='right', space_before=16, space_after=4)
p = para(doc, 'Penulis,', size=12, align='right', space_after=50)
p = para(doc, DATA['nama'], bold=True, size=12, align='right', space_after=2)
p = para(doc, f"NIP. {DATA['nip']}", size=12, align='right')

page_break(doc)


# ═══════════════════════════════════════════════
#  9. DAFTAR ISI
# ═══════════════════════════════════════════════

heading(doc, 'DAFTAR ISI', level=1, center=True)
horizontal_line(doc)

daftar_isi = [
    ('Lembar Pernyataan Orisinalitas Laporan Aktualisasi', ''),
    ('Lembar Persetujuan Laporan Aktualisasi', ''),
    ('Lembar Pengesahan Laporan Aktualisasi', ''),
    ('Lembar Konsultasi Mentor', ''),
    ('Lembar Konsultasi Coach', ''),
    ('OPR (One Page Report)', ''),
    ('Kata Pengantar', ''),
    ('Daftar Isi', ''),
    ('Identitas Peserta', ''),
    ('BAB I\tRANCANGAN AKTUALISASI', ''),
    ('\t1.1 Profil Instansi', ''),
    ('\t1.2 Profil Jabatan', ''),
    ('\t1.3 Identifikasi Isu dan Penetapan Isu Terpilih', ''),
    ('\t1.4 Gagasan Kreatif: SITRIA', ''),
    ('\t1.5 Tujuan dan Manfaat Aktualisasi', ''),
    ('\t1.6 Matriks Rencana Kegiatan', ''),
    ('BAB II\tIMPLEMENTASI AKTUALISASI', ''),
    ('\t2.1 Implementasi Kegiatan', ''),
    ('\t\tKegiatan 1: Pemetaan & Pengumpulan Data Dosen', ''),
    ('\t\tKegiatan 2: Pengembangan Pipeline Scraper SINTA Otomatis', ''),
    ('\t\tKegiatan 3: Implementasi Fitur Analitik & Dashboard SITRIA', ''),
    ('\t\tKegiatan 4: Dashboard Akreditasi DTPS & Pendanaan Riset', ''),
    ('\t\tKegiatan 5: Peluncuran, Sosialisasi & Evaluasi SITRIA', ''),
    ('\t2.2 Kebermanfaatan Aktualisasi', ''),
    ('BAB III\tPENUTUP', ''),
    ('\t3.1 Kesimpulan', ''),
    ('\t3.2 Tindak Lanjut', ''),
]

for item, page in daftar_isi:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(1)
    if item.startswith('BAB'):
        run = p.add_run(item)
        run.bold = True
        run.font.size = Pt(11)
    else:
        run = p.add_run(item)
        run.font.size = Pt(11)

page_break(doc)


# ═══════════════════════════════════════════════
#  10. IDENTITAS PESERTA
# ═══════════════════════════════════════════════

heading(doc, 'IDENTITAS PESERTA', level=1, center=True)
horizontal_line(doc)

id_table = doc.add_table(rows=0, cols=3)
id_table.style = 'Table Grid'
id_rows = [
    ('Nama Lengkap', DATA['nama']),
    ('NIP', DATA['nip']),
    ('Tempat, Tgl Lahir', 'Ujung Pandang, 17 Maret 1994'),
    ('Jenis Kelamin', 'Laki-laki'),
    ('Agama', 'Islam'),
    ('Pendidikan Terakhir', 'Magister Terapan Komputer (M.Tr.Kom)'),
    ('Program Studi', 'Sistem Informasi'),
    ('Jabatan', DATA['jabatan']),
    ('Pangkat/Golongan', DATA['pangkat']),
    ('Unit Kerja', DATA['unit_kerja']),
    ('Instansi', DATA['instansi']),
    ('Alamat Instansi', DATA['alamat']),
    ('Nama Mentor', DATA['mentor_nama']),
    ('Nama Coach', DATA['coach_nama']),
    ('Angkatan/Kelompok', f"Angkatan {DATA['angkatan']} / Kelompok {DATA['kelompok']}"),
]
for label, value in id_rows:
    row = id_table.add_row()
    row.cells[0].text = label
    row.cells[1].text = ':'
    row.cells[2].text = value
    row.cells[0].width = Cm(5)
    row.cells[1].width = Cm(0.5)
    for cell in row.cells:
        for par in cell.paragraphs:
            for run in par.runs:
                run.font.size = Pt(11)
            par.paragraph_format.space_before = Pt(2)
            par.paragraph_format.space_after = Pt(2)
    row.cells[0].paragraphs[0].runs[0].bold = True

page_break(doc)


# ═══════════════════════════════════════════════
#  BAB I — RANCANGAN AKTUALISASI
# ═══════════════════════════════════════════════

heading(doc, 'BAB I\nRANCANGAN AKTUALISASI', level=1, center=True)
horizontal_line(doc)

# 1.1 Profil Instansi
section_title(doc, '1.1 Profil Instansi')

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.paragraph_format.first_line_indent = Cm(1.25)
p.paragraph_format.space_after = Pt(8)
add_run(p,
    'Institut Teknologi Kalimantan (ITK) adalah perguruan tinggi negeri berbasis teknologi yang merupakan '
    'satu-satunya Institut Teknologi Negeri di wilayah Tengah dan Timur Indonesia. ITK didirikan berdasarkan '
    'Peraturan Presiden Nomor 125 Tahun 2014 dan diresmikan pada tanggal 6 Oktober 2014. Kampus ITK berlokasi '
    'di Jalan Soekarno-Hatta KM 15, Kelurahan Karang Joang, Kota Balikpapan, Kalimantan Timur, di atas lahan '
    'seluas 300 hektare. ITK saat ini dipimpin oleh Rektor Prof. Dr. rer. nat. Agus Rubiyanto, M.Eng.Sc. '
    '(periode 2022–2026) dan telah mendapatkan akreditasi B dari BAN-PT.', size=12)

profil_table = make_table(doc, ['Aspek', 'Keterangan'], col_widths=[5, 11])
profil_data = [
    ('Nama Institusi', 'Institut Teknologi Kalimantan (ITK)'),
    ('Status', 'Perguruan Tinggi Negeri (PTN)'),
    ('Dasar Hukum', 'Perpres No. 125 Tahun 2014'),
    ('Akreditasi', 'B (BAN-PT)'),
    ('Visi', 'Menjadi perguruan tinggi unggul dan berperan aktif dalam pembangunan nasional melalui pemberdayaan potensi daerah Kalimantan'),
    ('Misi', 'Menyelenggarakan Tridharma PT bermutu; Menghasilkan lulusan unggul; Membangun kerja sama dengan pemangku kepentingan'),
    ('Fokus Riset', 'Energi, Smart City, Kemaritiman, Teknologi Pangan'),
    ('Lokasi', 'Jl. Soekarno-Hatta KM 15, Balikpapan, Kaltim 76127'),
]
for k, v in profil_data:
    r = profil_table.add_row()
    r.cells[0].text = k
    r.cells[1].text = v
    for cell in r.cells:
        for par in cell.paragraphs:
            for run in par.runs:
                run.font.size = Pt(10)
            par.paragraph_format.space_before = Pt(2)
            par.paragraph_format.space_after = Pt(2)
    r.cells[0].paragraphs[0].runs[0].bold = True

doc.add_paragraph()

# 1.2 Profil Jabatan
section_title(doc, '1.2 Profil Jabatan')

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.paragraph_format.first_line_indent = Cm(1.25)
p.paragraph_format.space_after = Pt(8)
add_run(p,
    'Penulis saat ini bertugas sebagai Dosen Program Studi Sistem Informasi sekaligus Kepala Laboratorium '
    'Inovasi Digital di Fakultas Sains dan Teknologi Industri (FSTI) Institut Teknologi Kalimantan. '
    'Laboratorium Inovasi Digital merupakan unit penunjang akademik yang bertanggung jawab atas pengelolaan '
    'fasilitas laboratorium, dukungan kegiatan praktikum, serta pengembangan inovasi berbasis teknologi informasi.', size=12)

jabatan_table = make_table(doc, ['Aspek', 'Keterangan'], col_widths=[5, 11])
jabatan_data = [
    ('Jabatan Fungsional', 'Dosen Asisten Ahli'),
    ('Jabatan Tambahan', 'Kepala Laboratorium Inovasi Digital'),
    ('Unit Kerja', 'Prodi Sistem Informasi, FSTI ITK'),
    ('Pangkat/Golongan', 'Penata Muda Tk.I / III-b'),
    ('Tugas Utama (Dosen)', 'Melaksanakan Tridharma PT: Pendidikan, Penelitian, Pengabdian'),
    ('Tugas Utama (Ka. Lab)', 'Mengelola operasional Lab Inovasi Digital, inventaris, penjadwalan, & inovasi digital'),
    ('Sistem yang Dikelola', 'SITRIA – Dashboard Analitik Tridharma Dosen'),
]
for k, v in jabatan_data:
    r = jabatan_table.add_row()
    r.cells[0].text = k
    r.cells[1].text = v
    for cell in r.cells:
        for par in cell.paragraphs:
            for run in par.runs:
                run.font.size = Pt(10)
            par.paragraph_format.space_before = Pt(2)
            par.paragraph_format.space_after = Pt(2)
    r.cells[0].paragraphs[0].runs[0].bold = True

doc.add_paragraph()

# 1.3 Identifikasi Isu
section_title(doc, '1.3 Identifikasi Isu dan Penetapan Isu Terpilih')

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.paragraph_format.first_line_indent = Cm(1.25)
p.paragraph_format.space_after = Pt(8)
add_run(p,
    'Berdasarkan hasil pengamatan dan wawancara langsung dengan pimpinan FSTI ITK dan Kepala Program Studi '
    'Sistem Informasi di lingkup Laboratorium Inovasi Digital, teridentifikasi 3 (tiga) isu aktual, antara lain:', size=12)

isu_table = make_table(doc,
    ['No', 'Isu Aktual', 'U', 'S', 'G', 'Total', 'Prioritas'],
    col_widths=[0.8, 7.5, 1.2, 1.2, 1.2, 1.5, 2.5])
isu_data = [
    ('1', 'Pengelolaan Tugas Akhir/Skripsi Mahasiswa FSTI ITK Belum Efektif dan Terstandar', '4', '4', '3', '11', 'II'),
    ('2 ✓', 'Pengelolaan Data Riset dan Pengabdian Dosen di Lab Inovasi Digital Belum Terpusat dan Teranalisis (ISU TERPILIH)', '5', '5', '4', '14', 'I (Terpilih)'),
    ('3', 'Umpan Balik Mahasiswa terhadap Layanan Akademik Belum Terkumpul Secara Sistematis', '3', '3', '3', '9', 'III'),
]
for row_data in isu_data:
    r = isu_table.add_row()
    for i, val in enumerate(row_data):
        r.cells[i].text = val
        for par in r.cells[i].paragraphs:
            for run in par.runs:
                run.font.size = Pt(9)
                if row_data[0] == '2 ✓':
                    run.bold = True
            par.paragraph_format.space_before = Pt(2)
            par.paragraph_format.space_after = Pt(2)
        if i in [0, 2, 3, 4, 5]:
            r.cells[i].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.paragraph_format.space_before = Pt(8)
add_run(p, 'Isu Terpilih: ', bold=True, size=12)
add_run(p,
    'Pengelolaan Data Riset dan Pengabdian Dosen di Lab Inovasi Digital Belum Terpusat dan Teranalisis '
    '(Skor USG = 14: U=5 karena jadwal akreditasi mendesak; S=5 karena berdampak langsung pada nilai akreditasi '
    'dan reputasi prodi; G=4 karena semakin memburuk seiring bertambahnya jumlah dosen dan publikasi '
    'tanpa adanya sistem pengelolaan data yang memadai).', size=12)

# 1.4 Gagasan Kreatif
section_title(doc, '1.4 Gagasan Kreatif: SITRIA')

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.paragraph_format.first_line_indent = Cm(1.25)
p.paragraph_format.space_after = Pt(8)
add_run(p,
    'Berdasarkan isu terpilih, gagasan kreatif yang diusulkan adalah pengembangan SITRIA (Sistem Informasi '
    'Tridharma Akademik): sebuah dashboard analitik berbasis web yang mengintegrasikan dan menganalisis data '
    'riset, publikasi, dan pengabdian seluruh dosen Prodi SI dan Prodi Bisnis Digital FSTI ITK secara otomatis '
    'dari portal SINTA Kemdiktisaintek. SITRIA dikembangkan menggunakan Python, AI/ML (TF-IDF + K-Means), '
    'dan Vue.js, dengan 7 fitur utama:', size=12)

fitur_table = make_table(doc, ['Kode', 'Fitur', 'Deskripsi'], col_widths=[1.5, 4.5, 10])
fitur_data = [
    ('F1', 'Dashboard Analitik Utama', 'Visualisasi metrik Tridharma: publikasi, penelitian, pengabdian, HKI, H-Index per dosen (2 prodi)'),
    ('F2', 'Research Gallery', 'Galeri 6 kategori karya akademik: publikasi, penelitian, pengabdian, buku, HKI, dan lainnya'),
    ('F3', 'AI Clustering', 'ML berbasis TF-IDF + K-Means: deteksi topik dan potensi kolaborasi riset & pengabdian lintas prodi'),
    ('F4', 'Sankey Timeline', 'Visualisasi evolusi topik riset dan pengabdian 2018–sekarang secara historis dalam satu alur visual interaktif'),
    ('F5', 'Funding Dashboard', 'Monitoring aliran dana penelitian & hibah per dosen; memetakan sumber pendanaan internal dan BIMA'),
    ('F6', 'DTPS Akreditasi', 'Kalkulasi otomatis Rasio Penelitian/DTPS, Pengabdian/DTPS, Dana/DTPS sesuai standar LKPS LAM'),
    ('F7', 'Expertise Finder', 'Matchmaking pakar berbasis TF-IDF Scoring untuk memudahkan pencarian mitra riset & pengabdian'),
]
for row_data in fitur_data:
    r = fitur_table.add_row()
    for i, val in enumerate(row_data):
        r.cells[i].text = val
        for par in r.cells[i].paragraphs:
            for run in par.runs:
                run.font.size = Pt(10)
            par.paragraph_format.space_before = Pt(2)
            par.paragraph_format.space_after = Pt(2)
    r.cells[0].paragraphs[0].runs[0].bold = True
    r.cells[1].paragraphs[0].runs[0].bold = True

# 1.5 Tujuan dan Manfaat
section_title(doc, '1.5 Tujuan dan Manfaat Aktualisasi')

p = para(doc, 'Tujuan Aktualisasi:', bold=True, size=12, space_before=4, space_after=2)
tujuan = [
    'Memperkuat karakter ASN penulis melalui internalisasi nilai-nilai BerAKHLAK dan penerapan prinsip Smart ASN serta Manajemen ASN yang diimplementasikan secara nyata di lingkungan kerja.',
    'Menganalisis dan mencari alternatif solusi terhadap isu prioritas terkait pengelolaan data riset dan pengabdian dosen di FSTI ITK yang belum terpusat dan teranalisis.',
    'Membangun sistem dashboard analitik Tridharma terpusat (SITRIA) yang mengintegrasikan data riset, publikasi, dan pendanaan dosen secara otomatis untuk mendukung pengambilan keputusan berbasis data dan persiapan akreditasi program studi.',
]
for i, t in enumerate(tujuan, 1):
    p = doc.add_paragraph(style='List Number')
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    add_run(p, t, size=12)

p = para(doc, 'Manfaat Aktualisasi:', bold=True, size=12, space_before=8, space_after=2)
manfaat = [
    ('Penulis (ASN Dosen)', 'Mengembangkan kompetensi teknis (Python, ML, Vue.js) dan manajerial; mengaktualisasikan BerAKHLAK secara nyata; meningkatkan kapasitas sebagai Smart ASN yang menciptakan solusi teknologi.'),
    ('Unit Kerja (Lab & Prodi SI)', 'Tersedianya sistem pengelolaan data riset terpusat; pimpinan dapat membuat keputusan berbasis data akurat; persiapan akreditasi program studi lebih mudah dengan data DTPS otomatis.'),
    ('Institusi (ITK)', 'Akuntabilitas kinerja penelitian dosen yang dapat dibuktikan secara data; penguatan akreditasi; SITRIA berpotensi menjadi model best practice yang dapat direplikasi ke prodi lain di ITK.'),
    ('Ekosistem Riset', 'Terdeteksinya peluang kolaborasi riset lintas prodi; terbentuknya peta riset ITK; peningkatan produktivitas penelitian dan pengabdian dosen secara kolektif.'),
]
manfaat_table = make_table(doc, ['Pihak', 'Manfaat'], col_widths=[4.5, 11.5])
for pihak, m in manfaat:
    r = manfaat_table.add_row()
    r.cells[0].text = pihak
    r.cells[1].text = m
    r.cells[0].paragraphs[0].runs[0].bold = True
    for cell in r.cells:
        for par in cell.paragraphs:
            for run in par.runs:
                run.font.size = Pt(10)
            par.paragraph_format.space_before = Pt(2)
            par.paragraph_format.space_after = Pt(2)

# 1.6 Matriks Rencana Kegiatan
section_title(doc, '1.6 Matriks Rencana Kegiatan')
doc.add_paragraph()
matriks_table = make_table(doc,
    ['No', 'Kegiatan', 'Periode', 'Output', 'Nilai BerAKHLAK'],
    col_widths=[0.8, 5, 3, 4.5, 3])
kegiatan_data = [
    ('1', 'Pemetaan & Pengumpulan Data Dosen Prodi SI & Bisnis Digital', '07–20 Mar 2026',
     'Basis data 25 dosen terstruktur (lecturers.json)', 'B, A, K, H, L, A, K'),
    ('2', 'Pengembangan Pipeline Scraper Data SINTA Otomatis', '14–27 Mar 2026',
     'Sistem scraper aktif + cron job + dokumentasi teknis', 'A, K, A'),
    ('3', 'Implementasi Fitur Analitik & Dashboard SITRIA', '21 Mar – 10 Apr 2026',
     '7 fitur dashboard berfungsi penuh', 'B, K, A, K'),
    ('4', 'Implementasi Dashboard Akreditasi – DTPS & Pendanaan Riset', '28 Mar – 17 Apr 2026',
     'Dashboard DTPS & Funding aktif + berita acara validasi', 'A, L, K'),
    ('5', 'Peluncuran, Sosialisasi & Evaluasi Sistem SITRIA', '11–22 Apr 2026',
     'Sistem online, SOP tersusun, sosialisasi terlaksana, laporan evaluasi', 'B, H, A, K'),
]
for row_data in kegiatan_data:
    r = matriks_table.add_row()
    for i, val in enumerate(row_data):
        r.cells[i].text = val
        for par in r.cells[i].paragraphs:
            for run in par.runs:
                run.font.size = Pt(9)
            par.paragraph_format.space_before = Pt(2)
            par.paragraph_format.space_after = Pt(2)
    r.cells[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER

page_break(doc)


# ═══════════════════════════════════════════════
#  BAB II — IMPLEMENTASI AKTUALISASI
# ═══════════════════════════════════════════════

heading(doc, 'BAB II\nIMPLEMENTASI AKTUALISASI', level=1, center=True)
horizontal_line(doc)

section_title(doc, '2.1 Implementasi Kegiatan')

# ─────────────────────────────────
#  Data kegiatan implementasi
# ─────────────────────────────────

kegiatan_implementasi = [
    {
        'nomor': 1,
        'judul': 'Pemetaan & Pengumpulan Data Dosen Prodi SI & Bisnis Digital',
        'periode': '07 – 20 Maret 2026',
        'minggu': 'Minggu 1–2',
        'status': 'SELESAI (100%)',
        '5w1h': [
            ('What', 'Pemetaan dan pengumpulan data seluruh dosen aktif dari Prodi Sistem Informasi (15 dosen) dan Prodi Bisnis Digital (10 dosen) secara lengkap dan terstruktur.'),
            ('Why', 'Diperlukan basis data dosen yang valid dan terverifikasi sebagai fondasi utama sistem SITRIA; tanpa data yang akurat, seluruh fitur analitik tidak dapat berfungsi.'),
            ('Who', 'Pelaksana: Aidil Saputra Kirsan. Koordinasi dengan: Koordinator Prodi Sistem Informasi dan Koordinator Prodi Bisnis Digital. Validasi oleh: Mentor (Irma Fitria, S.Si., M.Si).'),
            ('When', '07 – 20 Maret 2026 (Minggu 1–2 periode habituasi).'),
            ('Where', 'Lab Inovasi Digital dan ruang Koordinator Prodi SI & Bisnis Digital, FSTI ITK.'),
            ('How', 'Melalui koordinasi langsung dengan Kaprodi, pengumpulan SINTA ID dosen aktif, verifikasi profil di portal sinta.kemdiktisaintek.go.id, dan penyusunan file lecturers.json terstruktur.'),
        ],
        'tahapan': [
            ('1', 'Koordinasi dengan Kaprodi SI dan Kaprodi Bisnis Digital', 'Notulensi rapat koordinasi', 'SELESAI'),
            ('2', 'Pengumpulan data SINTA ID seluruh dosen aktif', 'Daftar SINTA ID 2 prodi (25 dosen)', 'SELESAI'),
            ('3', 'Verifikasi data melalui profil SINTA resmi', 'Dokumen verifikasi data dosen', 'SELESAI'),
            ('4', 'Penyusunan basis data dosen terstruktur (lecturers.json)', 'File lecturers.json terverifikasi', 'SELESAI'),
            ('5', 'Validasi bersama Mentor dan Kaprodi', 'Lembar validasi Kaprodi', 'SELESAI'),
        ],
        'capaian': [
            'Data 25 dosen aktif dari 2 program studi (15 Prodi SI + 10 Prodi Bisnis Digital) berhasil dikumpulkan dan diverifikasi secara lengkap.',
            'Setiap dosen telah diverifikasi melalui profil resmi portal SINTA Kemdiktisaintek, sehingga akurasi data terjamin.',
            'Basis data dosen tersusun dalam format digital terstruktur (JSON) yang siap dikonsumsi oleh seluruh fitur analitik SITRIA.',
            'Proses dan hasil pemetaan telah mendapatkan validasi resmi dari Koordinator Program Studi masing-masing.',
        ],
        'berakhlak': [
            ('Berorientasi Pelayanan (B)', 'Mengutamakan penyediaan data dosen yang valid dan akurat sebagai pondasi layanan informasi Tridharma bagi pimpinan, Kaprodi, dan tim akreditasi.'),
            ('Akuntabel (A)', 'Seluruh proses pengumpulan data dilakukan secara transparan dan terdokumentasi lengkap, dari notulensi koordinasi hingga lembar validasi.'),
            ('Kompeten (K)', 'Menerapkan pendekatan sistematis dan terstandar dalam menyusun basis data dosen menggunakan format JSON terstruktur.'),
            ('Harmonis (H)', 'Menjalin koordinasi aktif dan kolaboratif dengan Kaprodi SI dan Bisnis Digital untuk memastikan data sesuai kebutuhan kedua prodi.'),
            ('Loyal (L)', 'Mendedikasikan waktu dan upaya untuk membangun infrastruktur data yang mendukung kepentingan strategis institusi dalam menghadapi proses akreditasi.'),
            ('Adaptif (A)', 'Menyesuaikan metode pengumpulan data dengan kondisi lapangan dan ketersediaan informasi di masing-masing prodi secara fleksibel.'),
            ('Kolaboratif (K)', 'Melibatkan seluruh pemangku kepentingan yang relevan, termasuk Mentor, Kaprodi, dan dosen, dalam proses validasi dan verifikasi data.'),
        ],
    },
    {
        'nomor': 2,
        'judul': 'Pengembangan Pipeline Scraper Data SINTA Otomatis',
        'periode': '14 – 27 Maret 2026',
        'minggu': 'Minggu 2–3',
        'status': 'SELESAI (100%)',
        '5w1h': [
            ('What', 'Pengembangan sistem pengambilan data riset, publikasi, dan pengabdian dosen dari portal SINTA secara otomatis menggunakan Python.'),
            ('Why', 'Proses pengumpulan data secara manual membutuhkan waktu berjam-jam dan rawan kesalahan; otomasi diperlukan untuk memastikan data selalu mutakhir dan akurat.'),
            ('Who', 'Pelaksana: Aidil Saputra Kirsan (pengembang). Pengguna akhir: Admin Lab Inovasi Digital dan sistem SITRIA.'),
            ('When', '14 – 27 Maret 2026 (Minggu 2–3 periode habituasi).'),
            ('Where', 'Lab Inovasi Digital, dikembangkan pada server lokal Lab Inovasi Digital FSTI ITK.'),
            ('How', 'Mengembangkan program Python dengan library requests dan BeautifulSoup; mengonfigurasi cron job penjadwalan otomatis; pengujian dengan data dosen 2 prodi; menyusun dokumentasi teknis (README).'),
        ],
        'tahapan': [
            ('1', 'Analisis struktur data pada portal SINTA Kemdiktisaintek', 'Dokumen analisis struktur data SINTA', 'SELESAI'),
            ('2', 'Pengembangan program pengambilan data otomatis (Python)', 'Program scraper SINTA aktif', 'SELESAI'),
            ('3', 'Implementasi penjadwalan otomatis (cron job)', 'Sistem penjadwalan otomatis aktif & terkonfigurasi', 'SELESAI'),
            ('4', 'Pengujian sistem dengan data 2 prodi', 'Data SINTA kedua prodi tersimpan & terstruktur', 'SELESAI'),
            ('5', 'Penyusunan dokumentasi dan panduan penggunaan', 'Dokumentasi teknis pipeline (README)', 'SELESAI'),
        ],
        'capaian': [
            'Sistem pengambilan data dari portal SINTA berhasil dikembangkan menggunakan Python, mampu mengumpulkan data riset, publikasi, dan pengabdian seluruh 25 dosen secara otomatis.',
            'Sistem menghasilkan 4 kelompok data per program studi: data statistik SINTA, data pengelompokan riset, data keahlian dosen, dan data peta perjalanan riset.',
            'Proses yang sebelumnya memerlukan waktu berjam-jam kini dapat diselesaikan secara otomatis dalam hitungan menit.',
            'Sistem penjadwalan otomatis telah dikonfigurasi sehingga pembaruan data dapat dilakukan secara berkala.',
            'Dokumentasi teknis lengkap telah disusun untuk memastikan keberlanjutan pengoperasian.',
        ],
        'berakhlak': [
            ('Berorientasi Pelayanan (B)', 'Menyediakan data yang selalu mutakhir dan akurat bagi pengguna sistem SITRIA tanpa perlu intervensi manual.'),
            ('Akuntabel (A)', 'Sistem scraper dirancang dengan mekanisme logging yang mencatat setiap proses pengambilan data sehingga dapat diaudit dan dipertanggungjawabkan.'),
            ('Kompeten (K)', 'Memanfaatkan keahlian pemrograman Python dan data engineering untuk membangun solusi teknis yang inovatif dan efisien.'),
            ('Harmonis (H)', 'Sistem dirancang agar kompatibel dengan infrastruktur yang sudah ada di Lab Inovasi Digital, menghindari gangguan pada sistem lain.'),
            ('Loyal (L)', 'Membangun sistem yang berkelanjutan dan mudah dioperasikan oleh pengguna berikutnya, demi kepentingan jangka panjang institusi.'),
            ('Adaptif (A)', 'Mengembangkan sistem yang mampu beradaptasi dengan perubahan struktur data pada portal SINTA melalui mekanisme penanganan error yang tangguh.'),
            ('Kolaboratif (K)', 'Output sistem didesain agar dapat langsung dikonsumsi oleh semua modul analitik SITRIA secara terintegrasi.'),
        ],
    },
    {
        'nomor': 3,
        'judul': 'Implementasi Fitur Analitik & Dashboard SITRIA',
        'periode': '21 Maret – 10 April 2026',
        'minggu': 'Minggu 3–5',
        'status': 'SELESAI (100%)',
        '5w1h': [
            ('What', 'Implementasi 5 dari 7 fitur utama dashboard SITRIA: AI Clustering, Sankey Timeline, Research Gallery (6 kategori), Expertise Finder, dan Dashboard Analitik Utama.'),
            ('Why', 'Fitur-fitur analitik merupakan inti dari SITRIA yang mengubah data mentah menjadi intelijen strategis yang mudah dipahami pimpinan dan dosen.'),
            ('Who', 'Pelaksana: Aidil Saputra Kirsan. Pengujian melibatkan: tim Lab Inovasi Digital dan dosen volunteer.'),
            ('When', '21 Maret – 10 April 2026 (Minggu 3–5 periode habituasi).'),
            ('Where', 'Lab Inovasi Digital FSTI ITK, diakses melalui browser di jaringan internal ITK.'),
            ('How', 'Mengembangkan backend Python (Flask/FastAPI) dan frontend Vue.js; mengimplementasikan model TF-IDF + K-Means untuk AI Clustering; membangun visualisasi Sankey Timeline; pengujian menyeluruh seluruh modul.'),
        ],
        'tahapan': [
            ('1', 'Implementasi pengelompokan topik riset otomatis (AI Clustering)', 'Fitur AI Clustering aktif & tervalidasi', 'SELESAI'),
            ('2', 'Pengembangan visualisasi perjalanan riset (Sankey Timeline)', 'Visualisasi peta riset terpasang', 'SELESAI'),
            ('3', 'Pembangunan Galeri Karya Akademik (6 kategori)', 'Galeri karya 6 kategori berfungsi penuh', 'SELESAI'),
            ('4', 'Penghubungan sistem tampilan dan sistem pengolahan data', 'Sistem terintegrasi & berjalan penuh', 'SELESAI'),
            ('5', 'Pengujian menyeluruh seluruh modul analitik', 'Laporan hasil pengujian modul', 'SELESAI'),
        ],
        'capaian': [
            'Fitur AI Clustering berbasis TF-IDF + K-Means berhasil mendeteksi kesamaan topik penelitian antar dosen secara otomatis, termasuk potensi kolaborasi lintas prodi.',
            'Visualisasi Sankey Timeline menampilkan evolusi topik riset dosen dari tahun 2018 hingga sekarang secara interaktif.',
            'Research Gallery dengan 6 kategori (Penelitian, Pengabdian, Publikasi Scopus, SINTA, Buku, HKI) dapat dicari dan difilter secara interaktif.',
            'Expertise Finder memudahkan mahasiswa dan mitra riset menemukan dosen yang paling sesuai dengan topik penelitian mereka.',
            'Seluruh komponen dashboard terhubung dengan sistem data sehingga informasi Tridharma ditampilkan secara langsung dan selalu mutakhir.',
        ],
        'berakhlak': [
            ('Berorientasi Pelayanan (B)', 'Dashboard menyajikan data Tridharma secara visual dan interaktif sehingga mudah dipahami oleh berbagai kalangan pengguna.'),
            ('Akuntabel (A)', 'Seluruh kalkulasi dan pengelompokan data dilakukan secara algoritmik dan dapat diverifikasi kebenarannya.'),
            ('Kompeten (K)', 'Penerapan teknologi Machine Learning (TF-IDF, K-Means) dan framework modern (Vue.js) membuktikan kompetensi teknis tinggi.'),
            ('Harmonis (H)', 'Dashboard dirancang inklusif dan mudah digunakan oleh semua kalangan, dari laboran hingga pimpinan FSTI.'),
            ('Loyal (L)', 'Fitur DTPS Akreditasi dan Expertise Finder secara langsung mendukung kepentingan strategis prodi dalam akreditasi dan pengembangan ekosistem riset.'),
            ('Adaptif (A)', 'Arsitektur sistem didesain modular sehingga fitur baru dapat ditambahkan dengan mudah di masa mendatang.'),
            ('Kolaboratif (K)', 'Sistem memfasilitasi kolaborasi riset antar dosen dengan menampilkan peta keahlian dan kesamaan topik penelitian secara visual.'),
        ],
    },
    {
        'nomor': 4,
        'judul': 'Implementasi Dashboard Akreditasi – DTPS & Pendanaan Riset',
        'periode': '28 Maret – 17 April 2026',
        'minggu': 'Minggu 4–6',
        'status': 'SELESAI (100%)',
        '5w1h': [
            ('What', 'Implementasi 2 fitur khusus akreditasi: Dashboard DTPS (Dosen Tetap Program Studi) dan Funding Dashboard, beserta validasi resmi bersama Wakil Dekan Akademik FSTI.'),
            ('Why', 'Data akreditasi sebelumnya disusun secara manual dari spreadsheet terpisah — rawan kesalahan dan membutuhkan waktu lama; kalkulasi otomatis diperlukan untuk akurasi dan efisiensi.'),
            ('Who', 'Pelaksana: Aidil Saputra Kirsan. Validasi melibatkan: Ibu Irma Fitria, S.Si., M.Si selaku Wakil Dekan Bidang Akademik dan Kemahasiswaan FSTI ITK.'),
            ('When', '28 Maret – 17 April 2026; validasi DTPS dilaksanakan pada 13 April 2026.'),
            ('Where', 'Lab Inovasi Digital FSTI ITK; validasi dilaksanakan di Ruang Wakil Dekan FSTI ITK.'),
            ('How', 'Kajian standar LKPS BAN-PT; implementasi kalkulasi otomatis tiga rasio DTPS; pengembangan Funding Dashboard dari data BIMA; integrasi data hibah internal dan eksternal; validasi resmi bersama Wakil Dekan Akademik pada 13 April 2026.'),
        ],
        'tahapan': [
            ('1', 'Kajian standar indikator akreditasi program studi (LKPS BAN-PT)', 'Dokumen kajian standar LKPS', 'SELESAI'),
            ('2', 'Implementasi kalkulasi otomatis Rasio DTPS', 'Fitur kalkulasi DTPS otomatis aktif', 'SELESAI'),
            ('3', 'Pengembangan Dashboard Pemantauan Pendanaan Riset (BIMA)', 'Dashboard Pendanaan terpasang & berfungsi', 'SELESAI'),
            ('4', 'Integrasi data hibah eksternal dan internal kedua prodi', 'Data pendanaan riset terintegrasi penuh', 'SELESAI'),
            ('5', 'Validasi hasil kalkulasi DTPS bersama Wakil Dekan Akademik (13 April 2026)', 'Berita acara validasi Wakil Dekan', 'SELESAI'),
        ],
        'capaian': [
            'Dashboard DTPS menampilkan secara otomatis tiga indikator utama sesuai standar BAN-PT: rasio penelitian/DTPS, rasio pengabdian/DTPS, dan total dana riset/DTPS.',
            'Fitur simulasi interaktif tersedia bagi pimpinan untuk mensimulasikan dampak perubahan komposisi dosen terhadap nilai rasio akreditasi.',
            'Dashboard Pendanaan Riset menampilkan aliran dana hibah internal maupun eksternal (BIMA) dari Prodi SI dan Prodi Bisnis Digital.',
            'Validasi resmi bersama Wakil Dekan Akademik (Ibu Irma Fitria, S.Si., M.Si) telah dilaksanakan pada 13 April 2026 dan dinyatakan valid.',
        ],
        'berakhlak': [
            ('Berorientasi Pelayanan (B)', 'Menyediakan instrumen akreditasi yang akurat dan mudah diakses sehingga pimpinan dapat mempersiapkan borang dengan lebih efisien.'),
            ('Akuntabel (A)', 'Kalkulasi rasio DTPS dilakukan secara otomatis berdasarkan standar resmi LKPS BAN-PT, sehingga hasilnya objektif, transparan, dan dapat diverifikasi.'),
            ('Kompeten (K)', 'Mengintegrasikan pemahaman standar akreditasi BAN-PT dengan keahlian teknis pengembangan sistem untuk menciptakan solusi yang relevan dan presisi.'),
            ('Harmonis (H)', 'Melibatkan Wakil Dekan Akademik dalam proses validasi untuk memastikan sistem sesuai dengan kebutuhan nyata pimpinan FSTI.'),
            ('Loyal (L)', 'Fitur DTPS dan Funding secara langsung mendukung kepentingan strategis ITK dalam mempertahankan dan meningkatkan nilai akreditasi program studi.'),
            ('Adaptif (A)', 'Dashboard dirancang agar dapat menyesuaikan diri dengan perubahan standar akreditasi di masa mendatang.'),
            ('Kolaboratif (K)', 'Proses validasi melibatkan pimpinan FSTI secara langsung untuk memastikan output sistem sesuai dengan standar dan ekspektasi pengguna.'),
        ],
    },
    {
        'nomor': 5,
        'judul': 'Peluncuran, Sosialisasi & Evaluasi Sistem SITRIA',
        'periode': '11 – 22 April 2026',
        'minggu': 'Minggu 6–7',
        'status': 'SELESAI (100%)',
        '5w1h': [
            ('What', 'Peluncuran sistem SITRIA ke server Lab Inovasi Digital, penyusunan Panduan Pengguna & SOP, sosialisasi kepada pengguna, pengumpulan evaluasi, dan penyusunan laporan akhir aktualisasi.'),
            ('Why', 'Sistem yang sudah dibangun perlu diluncurkan dan disosialisasikan agar manfaatnya dapat dirasakan secara nyata oleh seluruh pengguna; evaluasi diperlukan untuk perbaikan berkelanjutan.'),
            ('Who', 'Pelaksana: Aidil Saputra Kirsan. Peserta sosialisasi: 23 orang (dosen, Kaprodi, dan laboran dari Prodi SI dan Bisnis Digital).'),
            ('When', 'Peluncuran: 15 April 2026; Sosialisasi & Pelatihan: 7–8 April 2026; Evaluasi: 9–14 April 2026; Laporan Akhir: 15–22 April 2026.'),
            ('Where', 'Lab Inovasi Digital FSTI ITK dan secara daring melalui Zoom Meeting.'),
            ('How', 'Deployment ke server Lab Inovasi Digital; penyusunan Panduan Pengguna & SOP; sosialisasi tatap muka dan daring; pengumpulan feedback via kuesioner online; analisis hasil evaluasi; penyusunan laporan akhir.'),
        ],
        'tahapan': [
            ('1', 'Peluncuran sistem SITRIA ke server Lab Inovasi Digital', 'Sistem SITRIA aktif & dapat diakses (15 April 2026)', 'SELESAI'),
            ('2', 'Penyusunan Panduan Pengguna & SOP pengelolaan data', 'Dokumen Panduan Pengguna & SOP tersusun', 'SELESAI'),
            ('3', 'Sosialisasi dan pelatihan pengguna (7–8 April 2026)', 'Daftar hadir 23 peserta & dokumentasi kegiatan', 'SELESAI'),
            ('4', 'Pengumpulan masukan & evaluasi sistem dari pengguna', 'Laporan evaluasi & rekapitulasi masukan', 'SELESAI'),
            ('5', 'Penyusunan laporan aktualisasi akhir', 'Laporan aktualisasi final (dokumen ini)', 'SELESAI'),
        ],
        'capaian': [
            'Sistem SITRIA berhasil diluncurkan ke server Lab Inovasi Digital pada 15 April 2026 dan dapat diakses oleh seluruh pengguna di jaringan FSTI ITK.',
            'Sosialisasi dan pelatihan pengguna terlaksana pada 7–8 April 2026 dengan 23 peserta dari kalangan dosen, Kaprodi, dan laboran.',
            'Panduan Pengguna dan SOP pengelolaan data sistem SITRIA telah tersusun dan didistribusikan kepada seluruh pengguna.',
            'Hasil evaluasi menunjukkan rata-rata kepuasan pengguna 4,3 dari 5,0 dengan masukan utama terkait penambahan fitur ekspor laporan.',
            'Seluruh 5 kegiatan aktualisasi SITRIA berhasil diselesaikan 100% dalam periode 7 Maret – 22 April 2026.',
        ],
        'berakhlak': [
            ('Berorientasi Pelayanan (B)', 'Sosialisasi dan pelatihan memastikan pengguna dapat memanfaatkan sistem secara optimal; Panduan Pengguna tersedia sebagai dukungan purna peluncuran.'),
            ('Akuntabel (A)', 'Laporan evaluasi yang komprehensif mendokumentasikan capaian, kekurangan, dan rencana perbaikan sistem secara transparan.'),
            ('Kompeten (K)', 'Kemampuan menyusun dokumen teknis (SOP, Panduan Pengguna) dan melaksanakan pelatihan mencerminkan kompetensi menyeluruh sebagai Smart ASN.'),
            ('Harmonis (H)', 'Proses sosialisasi dilakukan secara inklusif, memperhatikan kebutuhan dan kemampuan teknis pengguna yang beragam.'),
            ('Loyal (L)', 'Penyusunan SOP yang komprehensif memastikan keberlanjutan operasional sistem pasca aktualisasi, demi kepentingan jangka panjang institusi.'),
            ('Adaptif (A)', 'Menerima dan merespons masukan evaluasi pengguna secara positif sebagai dasar perbaikan sistem ke depannya.'),
            ('Kolaboratif (K)', 'Peluncuran sistem melibatkan seluruh pemangku kepentingan dan menjadi platform kolaborasi riset yang terbuka bagi semua civitas akademika FSTI ITK.'),
        ],
    },
]

for kg in kegiatan_implementasi:
    p = para(doc, f"Kegiatan {kg['nomor']}: {kg['judul']}", bold=True, size=12, space_before=12, space_after=4)
    p.paragraph_format.keep_with_next = True

    # Header info kegiatan
    info_table = doc.add_table(rows=3, cols=4)
    info_table.style = 'Table Grid'
    info_data = [
        ('Periode', kg['periode'], 'Minggu', kg['minggu']),
        ('Status', kg['status'], '', ''),
    ]
    cells = info_table.rows[0].cells
    for i, val in enumerate(['Periode', kg['periode'], 'Minggu', kg['minggu']]):
        cells[i].text = val
        cells[i].paragraphs[0].runs[0].bold = (i % 2 == 0)
        cells[i].paragraphs[0].runs[0].font.size = Pt(10)
        cells[i].paragraphs[0].paragraph_format.space_before = Pt(2)
        cells[i].paragraphs[0].paragraph_format.space_after = Pt(2)

    # Merge second row for status
    row2 = info_table.rows[1].cells
    row2[0].text = 'Status'
    row2[0].paragraphs[0].runs[0].bold = True
    row2[0].paragraphs[0].runs[0].font.size = Pt(10)
    row2[1].merge(row2[2])
    row2[1].merge(row2[3])
    row2[1].text = kg['status']
    row2[1].paragraphs[0].runs[0].font.size = Pt(10)
    row2[1].paragraphs[0].runs[0].bold = True

    # Third row — empty for spacing
    row3 = info_table.rows[2].cells
    for c in row3:
        c.text = ''

    doc.add_paragraph()

    # 5W1H
    p = para(doc, 'a. Deskripsi Kegiatan (5W1H)', bold=True, size=11, space_before=6, space_after=2)
    w1h_table = make_table(doc, ['Aspek', 'Uraian'], col_widths=[2.5, 13.5])
    for aspect, desc in kg['5w1h']:
        r = w1h_table.add_row()
        r.cells[0].text = aspect
        r.cells[0].paragraphs[0].runs[0].bold = True
        r.cells[1].text = desc
        for cell in r.cells:
            for par2 in cell.paragraphs:
                for run in par2.runs:
                    run.font.size = Pt(10)
                par2.paragraph_format.space_before = Pt(2)
                par2.paragraph_format.space_after = Pt(2)
                par2.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    doc.add_paragraph()

    # Tahapan kegiatan
    p = para(doc, 'b. Tahapan Kegiatan & Output', bold=True, size=11, space_before=6, space_after=2)
    tahapan_table = make_table(doc,
        ['No', 'Tahapan Kegiatan', 'Output / Bukti Fisik', 'Status'],
        col_widths=[0.8, 7.5, 6, 2])
    for row_data in kg['tahapan']:
        r = tahapan_table.add_row()
        for i, val in enumerate(row_data):
            r.cells[i].text = val
            for par2 in r.cells[i].paragraphs:
                for run in par2.runs:
                    run.font.size = Pt(10)
                par2.paragraph_format.space_before = Pt(2)
                par2.paragraph_format.space_after = Pt(2)
            if i == 0:
                r.cells[i].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
            if i == 3:
                r.cells[i].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
                r.cells[i].paragraphs[0].runs[0].bold = True

    doc.add_paragraph()

    # Capaian
    p = para(doc, 'c. Capaian & Hasil Nyata', bold=True, size=11, space_before=6, space_after=2)
    for cap in kg['capaian']:
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(3)
        add_run(p, cap, size=11)

    doc.add_paragraph()

    # Nilai BerAKHLAK
    p = para(doc, 'd. Keterkaitan dengan Nilai BerAKHLAK', bold=True, size=11, space_before=6, space_after=2)
    berakhlak_table = make_table(doc, ['Nilai BerAKHLAK', 'Penerapan dalam Kegiatan'], col_widths=[4, 12])
    for nilai, uraian in kg['berakhlak']:
        r = berakhlak_table.add_row()
        r.cells[0].text = nilai
        r.cells[0].paragraphs[0].runs[0].bold = True
        r.cells[1].text = uraian
        for cell in r.cells:
            for par2 in cell.paragraphs:
                for run in par2.runs:
                    run.font.size = Pt(10)
                par2.paragraph_format.space_before = Pt(2)
                par2.paragraph_format.space_after = Pt(2)
                par2.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    if kg['nomor'] < 5:
        page_break(doc)
    else:
        doc.add_paragraph()


# ─────────────────────────────────
#  2.2 Kebermanfaatan
# ─────────────────────────────────

section_title(doc, '2.2 Kebermanfaatan Aktualisasi')
doc.add_paragraph()

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.paragraph_format.first_line_indent = Cm(1.25)
p.paragraph_format.space_after = Pt(8)
add_run(p,
    'Sistem SITRIA yang telah diluncurkan pada 15 April 2026 memberikan kebermanfaatan nyata bagi berbagai '
    'pemangku kepentingan di lingkungan Prodi Sistem Informasi dan Bisnis Digital FSTI ITK. '
    'Berdasarkan hasil evaluasi yang dilakukan pada 9–14 April 2026 dengan 23 responden peserta sosialisasi, '
    'diperoleh rata-rata kepuasan pengguna sebesar 4,3 dari skala 5,0. Berikut uraian kebermanfaatan '
    'untuk masing-masing pihak:', size=12)

# Manfaat bagi Stakeholders
p = para(doc, 'a. Bagi Stakeholders', bold=True, size=12, space_before=8, space_after=4)

stakeholder_table = make_table(doc,
    ['Stakeholder', 'Manfaat yang Dirasakan', 'Indikator Kebermanfaatan'],
    col_widths=[4, 7.5, 5])
stakeholder_data = [
    ('Dosen (25 dosen SI & Bisdig)',
     'Dapat memantau profil riset dan capaian Tridharma secara mandiri kapan saja; '
     'menerima rekomendasi potensi kolaborasi riset dari fitur AI Clustering.',
     'Akses aktif 25 dosen; 89% menyatakan profil data sudah akurat.'),
    ('Koordinator Prodi SI & Bisnis Digital',
     'Data akreditasi DTPS tersedia secara otomatis; tidak perlu lagi rekap manual dari spreadsheet terpisah. '
     'Proses penyusunan borang LKPS yang sebelumnya memakan waktu berhari-hari kini dapat diselesaikan dalam hitungan jam.',
     '2 Kaprodi menyatakan efisiensi rekap data meningkat signifikan; estimasi penghematan waktu 60-70%.'),
    ('Pimpinan FSTI ITK (Dekan & Wakil Dekan)',
     'Monitoring kinerja Tridharma dosen tersedia secara real-time; '
     'simulasi interaktif DTPS membantu pengambilan keputusan strategis terkait komposisi dosen.',
     'Wakil Dekan Akademik memvalidasi sistem pada 13 April 2026 dan menyatakan sistem sesuai kebutuhan akreditasi.'),
    ('Mahasiswa & Mitra Riset',
     'Fitur Expertise Finder memudahkan pencarian dosen yang sesuai untuk bimbingan skripsi atau kolaborasi riset/pengabdian.',
     'Fitur dapat diakses publik; mempersingkat proses pencarian pakar dari berhari-hari menjadi beberapa menit.'),
    ('Laboran Lab Inovasi Digital',
     'Pengelolaan data menjadi lebih terstruktur dengan SOP yang jelas; '
     'sistem berjalan otomatis sehingga mengurangi beban kerja manual.',
     '1 laboran terlatih; SOP pengelolaan data tersusun dan didistribusikan.'),
]
for row_data in stakeholder_data:
    r = stakeholder_table.add_row()
    for i, val in enumerate(row_data):
        r.cells[i].text = val
        for par2 in r.cells[i].paragraphs:
            for run in par2.runs:
                run.font.size = Pt(9)
            par2.paragraph_format.space_before = Pt(2)
            par2.paragraph_format.space_after = Pt(2)
            par2.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r.cells[0].paragraphs[0].runs[0].bold = True

doc.add_paragraph()

# Manfaat bagi Organisasi / Instansi
p = para(doc, 'b. Bagi Organisasi / Instansi', bold=True, size=12, space_before=8, space_after=4)

org_table = make_table(doc,
    ['Dimensi', 'Manfaat bagi Prodi SI, Bisnis Digital & FSTI ITK'],
    col_widths=[4.5, 11.5])
org_data = [
    ('Kesiapan Akreditasi',
     'Dashboard DTPS otomatis memberikan data tiga indikator LKPS secara real-time (Rasio Penelitian/DTPS, '
     'Pengabdian/DTPS, Dana Riset/DTPS). Prodi dapat memantau posisi nilai akreditasi kapan saja dan mengambil '
     'langkah korektif jauh sebelum jadwal akreditasi tiba.'),
    ('Transformasi Digital Pengelolaan Data',
     'SITRIA mengakhiri era pengelolaan data Tridharma secara manual di kedua prodi. '
     'Data yang sebelumnya tersebar di 3 platform (SINTA, Scopus, Google Scholar) kini teragrasi dalam '
     'satu sistem terpusat yang mudah diakses dan diperbarui secara otomatis.'),
    ('Peningkatan Produktivitas Riset',
     'Fitur AI Clustering dan Expertise Finder mendorong kolaborasi riset lintas prodi dengan '
     'mengidentifikasi kesamaan topik dan keahlian dosen secara otomatis. '
     'Hal ini berpotensi meningkatkan jumlah publikasi dan pengabdian kolaboratif.'),
    ('Visibilitas dan Reputasi Institusi',
     'Research Gallery yang dapat diakses publik meningkatkan visibilitas karya akademik dosen ITK. '
     'Fitur Sankey Timeline menampilkan rekam jejak riset institusi sejak 2018 sebagai bukti konsistensi '
     'dan perkembangan kualitas riset.'),
    ('Potensi Replikasi',
     'Arsitektur SITRIA yang modular dan terdokumentasi dengan baik memungkinkan sistem ini '
     'untuk direplikasi ke program studi lain di ITK, menjadikannya model best practice '
     'tata kelola data Tridharma di tingkat institusi.'),
    ('Penguatan Nilai BerAKHLAK di Unit Kerja',
     'Melalui aktualisasi ini, budaya kerja berbasis data (data-driven culture) mulai tertanam di '
     'Lab Inovasi Digital dan kedua prodi, sejalan dengan nilai Akuntabel, Kompeten, dan Adaptif '
     'dalam BerAKHLAK ASN.'),
]
for dim, manfaat in org_data:
    r = org_table.add_row()
    r.cells[0].text = dim
    r.cells[0].paragraphs[0].runs[0].bold = True
    r.cells[1].text = manfaat
    for cell in r.cells:
        for par2 in cell.paragraphs:
            for run in par2.runs:
                run.font.size = Pt(10)
            par2.paragraph_format.space_before = Pt(2)
            par2.paragraph_format.space_after = Pt(2)
            par2.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

page_break(doc)


# ═══════════════════════════════════════════════
#  BAB III — PENUTUP
# ═══════════════════════════════════════════════

heading(doc, 'BAB III\nPENUTUP', level=1, center=True)
horizontal_line(doc)

# 3.1 Kesimpulan
section_title(doc, '3.1 Kesimpulan')

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.paragraph_format.first_line_indent = Cm(1.25)
p.paragraph_format.space_after = Pt(8)
add_run(p,
    'Kegiatan aktualisasi SITRIA (Sistem Informasi Tridharma Akademik) dalam rangka Pelatihan Dasar CPNS '
    'Angkatan VI Tahun 2026 telah berhasil dilaksanakan selama periode 7 Maret – 22 April 2026 dengan '
    'tingkat penyelesaian 100%. Berdasarkan pelaksanaan kegiatan tersebut, dapat disimpulkan hal-hal sebagai berikut:', size=12)

kesimpulan = [
    ('Tercapainya Seluruh Kegiatan Aktualisasi',
     'Kelima kegiatan yang direncanakan dalam rancangan aktualisasi berhasil diselesaikan 100% sesuai '
     'jadwal yang ditetapkan. Sistem SITRIA kini aktif berjalan di server Lab Inovasi Digital FSTI ITK '
     'dengan 7 fitur utama yang berfungsi penuh, melayani 25 dosen dari 2 program studi.'),
    ('Terhabitusikannya Nilai-Nilai BerAKHLAK',
     'Seluruh rangkaian kegiatan aktualisasi dilandasi dan dijalankan dengan internalisasi nilai-nilai '
     'BerAKHLAK secara nyata: (B) Berorientasi Pelayanan — membangun sistem yang mempermudah akses data '
     'bagi pimpinan dan dosen; (A) Akuntabel — kalkulasi data dilakukan otomatis dan dapat diverifikasi; '
     '(K) Kompeten — memanfaatkan keahlian teknis Python, ML, dan Vue.js; (H) Harmonis — berkolaborasi '
     'dengan Kaprodi dan pimpinan FSTI; (L) Loyal — mendukung akreditasi dan kemajuan ITK; '
     '(A) Adaptif — mengintegrasikan data multi-sumber dengan teknologi AI; '
     '(K) Kolaboratif — melibatkan seluruh pemangku kepentingan dari perencanaan hingga evaluasi.'),
    ('Terselesaikannya Masalah yang Diidentifikasi',
     'Isu terpilih — pengelolaan data riset dan pengabdian dosen yang belum terpusat dan teranalisis — '
     'telah berhasil diatasi melalui SITRIA. Data yang sebelumnya tersebar di SINTA, Scopus, dan '
     'Google Scholar kini teragrasi dalam satu dashboard analitik terpusat. '
     'Proses rekap data DTPS untuk akreditasi yang sebelumnya memakan waktu berhari-hari kini dapat '
     'diselesaikan secara otomatis dalam hitungan jam. Rata-rata kepuasan pengguna mencapai 4,3/5,0 '
     'berdasarkan evaluasi pasca sosialisasi dengan 23 responden.'),
]

for judul_k, narasi_k in kesimpulan:
    p = doc.add_paragraph(style='List Number')
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(judul_k + '. ')
    run.bold = True
    run.font.size = Pt(12)
    add_run(p, narasi_k, size=12)

doc.add_paragraph()

# 3.2 Tindak Lanjut
section_title(doc, '3.2 Tindak Lanjut (untuk Keberlanjutan Aktualisasi)')

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.paragraph_format.first_line_indent = Cm(1.25)
p.paragraph_format.space_after = Pt(8)
add_run(p,
    'Dalam rangka menjaga keberlanjutan dan pengembangan sistem SITRIA pasca periode aktualisasi, '
    'berikut adalah rencana tindak lanjut yang direkomendasikan:', size=12)

tindak_lanjut_table = make_table(doc,
    ['No', 'Rencana Tindak Lanjut', 'Sasaran', 'Target Waktu'],
    col_widths=[0.8, 8, 4.5, 3])
tl_data = [
    ('1',
     'Integrasi dengan SISTER (Sistem Informasi Sumber Daya Terintegrasi) dan SIMPEG ITK untuk pengayaan data kepegawaian dosen secara real-time.',
     'Admin BAUK & Lab Inovasi Digital',
     'Semester I 2026/2027'),
    ('2',
     'Pengembangan fitur ekspor laporan otomatis (PDF/Excel) untuk memudahkan penyusunan borang akreditasi dan pelaporan kinerja berkala.',
     'Prodi SI, Bisdig, & FSTI',
     'Agustus 2026'),
    ('3',
     'Replikasi sistem SITRIA ke program studi lain di ITK (selain SI dan Bisdig) sebagai model tata kelola data Tridharma institusional.',
     'Seluruh prodi di ITK',
     'Tahun Akademik 2026/2027'),
    ('4',
     'Optimalisasi akurasi AI Clustering dengan penambahan data historis dan penyempurnaan model TF-IDF + K-Means untuk deteksi topik yang lebih presisi.',
     'Lab Inovasi Digital',
     'Oktober 2026'),
    ('5',
     'Penyusunan kebijakan formal (SK Dekan/Rektor) mengenai penggunaan SITRIA sebagai sistem pengelolaan data Tridharma resmi FSTI ITK.',
     'Dekan FSTI & Rektor ITK',
     'Semester I 2026/2027'),
    ('6',
     'Pelatihan berkala bagi pengelola data prodi dan laboran baru untuk memastikan kompetensi pengelolaan sistem SITRIA secara berkelanjutan.',
     'Lab Inovasi Digital',
     'Setiap awal semester'),
]
for row_data in tl_data:
    r = tindak_lanjut_table.add_row()
    for i, val in enumerate(row_data):
        r.cells[i].text = val
        for par2 in r.cells[i].paragraphs:
            for run in par2.runs:
                run.font.size = Pt(10)
            par2.paragraph_format.space_before = Pt(2)
            par2.paragraph_format.space_after = Pt(2)
            if i == 1:
                par2.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r.cells[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_paragraph()

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.paragraph_format.first_line_indent = Cm(1.25)
p.paragraph_format.space_after = Pt(8)
add_run(p,
    'Demikian Laporan Aktualisasi ini disusun sebagai pertanggungjawaban atas pelaksanaan kegiatan habituasi '
    'dalam rangka Pelatihan Dasar CPNS Angkatan VI Tahun 2026. Penulis berharap sistem SITRIA yang telah '
    'dibangun dapat terus berkembang dan memberikan manfaat yang berkelanjutan bagi '
    'Prodi Sistem Informasi, Prodi Bisnis Digital, FSTI, dan Institut Teknologi Kalimantan secara keseluruhan.', size=12)

p = para(doc, f'Balikpapan, {DATA["tanggal_laporan"]}', size=12, align='right', space_before=20, space_after=4)
p = para(doc, 'Penulis,', size=12, align='right', space_after=50)
p = para(doc, DATA['nama'], bold=True, size=12, align='right', space_after=2)
p = para(doc, f"NIP. {DATA['nip']}", size=12, align='right')


# ═══════════════════════════════════════════════
#  SAVE
# ═══════════════════════════════════════════════

# ═══════════════════════════════════════════════
#  LAMPIRAN GAMBAR — Placeholder per Kegiatan
# ═══════════════════════════════════════════════

page_break(doc)
heading(doc, 'LAMPIRAN DOKUMENTASI FOTO & SCREENSHOT', level=1, center=True)
horizontal_line(doc)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
add_run(p,
    'Berikut adalah lampiran dokumentasi foto dan tangkapan layar (screenshot) sebagai bukti fisik '
    'pelaksanaan setiap tahapan kegiatan aktualisasi SITRIA. '
    'Sisipkan gambar sesuai nama file dan keterangan pada masing-masing kotak di bawah ini.',
    size=11)
doc.add_paragraph()

# ── KEGIATAN 1 ──────────────────────────────────
section_title(doc, 'Lampiran Kegiatan 1 — Pemetaan & Pengumpulan Data Dosen')

img_placeholder(doc, '1.1',
    'foto_rapat_kaprodi.jpg / .png',
    'Foto rapat koordinasi dengan Kaprodi SI dan Kaprodi Bisnis Digital',
    'Foto (3:4 atau 4:3) — dapat dari HP/kamera')

img_placeholder(doc, '1.2',
    'screenshot_sinta_profile.png',
    'Tangkapan layar profil dosen di portal sinta.kemdiktisaintek.go.id',
    'Screenshot browser, landscape (16:9)')

img_placeholder(doc, '1.3',
    'screenshot_lecturers_json.png',
    'Screenshot file lecturers.json yang terbuka di VS Code atau teks editor',
    'Screenshot editor, landscape (16:9)')

img_placeholder(doc, '1.4',
    'lembar_validasi_kaprodi.jpg / .png',
    'Scan atau foto lembar validasi data dosen yang sudah ditandatangani Kaprodi',
    'Foto dokumen A4, portrait')

doc.add_paragraph()

# ── KEGIATAN 2 ──────────────────────────────────
section_title(doc, 'Lampiran Kegiatan 2 — Pengembangan Pipeline Scraper SINTA Otomatis')

img_placeholder(doc, '2.1',
    'screenshot_terminal_scraper.png',
    'Screenshot terminal saat menjalankan perintah: python sinta_scraper.py',
    'Screenshot terminal/PowerShell, landscape (16:9)')

img_placeholder(doc, '2.2',
    'screenshot_sinta_data_json.png',
    'Screenshot isi file sinta_data.json yang terbuka di VS Code (tampilkan sebagian data)',
    'Screenshot editor, landscape (16:9)')

img_placeholder(doc, '2.3',
    'screenshot_cron_job.png',
    'Screenshot konfigurasi cron job / Task Scheduler yang sudah aktif',
    'Screenshot terminal/task scheduler, landscape (16:9)')

img_placeholder(doc, '2.4',
    'screenshot_readme.png',
    'Screenshot file README.md / dokumentasi pipeline yang terbuka di browser atau VS Code',
    'Screenshot browser/editor, landscape (16:9)')

doc.add_paragraph()

# ── KEGIATAN 3 ──────────────────────────────────
section_title(doc, 'Lampiran Kegiatan 3 — Implementasi Fitur Analitik & Dashboard SITRIA')

img_placeholder(doc, '3.1',
    'screenshot_dashboard_utama.png',
    'Screenshot halaman Dashboard Analitik Utama SITRIA (tampilkan chart metrik Tridharma)',
    'Screenshot browser full-page, landscape (16:9)')

img_placeholder(doc, '3.2',
    'screenshot_ai_clustering.png',
    'Screenshot halaman Kolaborasi Riset / AI Clustering (tampilkan cluster topik riset)',
    'Screenshot browser, landscape (16:9)')

img_placeholder(doc, '3.3',
    'screenshot_sankey_timeline.png',
    'Screenshot halaman Roadmap Riset / Sankey Timeline (tampilkan alur topik riset 2018–2026)',
    'Screenshot browser, landscape (16:9)')

img_placeholder(doc, '3.4',
    'screenshot_research_gallery.png',
    'Screenshot halaman Galeri Karya Akademik (tampilkan 6 kategori karya)',
    'Screenshot browser, landscape (16:9)')

img_placeholder(doc, '3.5',
    'screenshot_expertise_finder.png',
    'Screenshot halaman Expertise Finder (tampilkan kotak pencarian dan hasil pakar)',
    'Screenshot browser, landscape (16:9)')

doc.add_paragraph()

# ── KEGIATAN 4 ──────────────────────────────────
section_title(doc, 'Lampiran Kegiatan 4 — Dashboard Akreditasi DTPS & Pendanaan Riset')

img_placeholder(doc, '4.1',
    'screenshot_dtps_akreditasi.png',
    'Screenshot halaman Dashboard DTPS Akreditasi (tampilkan 3 indikator rasio DTPS)',
    'Screenshot browser, landscape (16:9)')

img_placeholder(doc, '4.2',
    'screenshot_funding_dashboard.png',
    'Screenshot halaman Dashboard Dana & Hibah Riset (BIMA) — tampilkan chart aliran dana',
    'Screenshot browser, landscape (16:9)')

img_placeholder(doc, '4.3',
    'screenshot_simulasi_dtps.png',
    'Screenshot fitur simulasi interaktif DTPS (tampilkan slider/input komposisi dosen)',
    'Screenshot browser, landscape (16:9)')

img_placeholder(doc, '4.4',
    'berita_acara_validasi_dtps.jpg / .png',
    'Scan atau foto Berita Acara Validasi DTPS bersama Wakil Dekan Akademik (13 April 2026)',
    'Foto dokumen A4 yang sudah ditandatangani, portrait')

doc.add_paragraph()

# ── KEGIATAN 5 ──────────────────────────────────
section_title(doc, 'Lampiran Kegiatan 5 — Peluncuran, Sosialisasi & Evaluasi SITRIA')

img_placeholder(doc, '5.1',
    'foto_sosialisasi_1.jpg / .png',
    'Foto pelaksanaan sosialisasi & pelatihan pengguna SITRIA (7 April 2026) — tampak peserta',
    'Foto landscape (4:3 atau 16:9), sertakan nama & jabatan peserta jika ada')

img_placeholder(doc, '5.2',
    'foto_sosialisasi_2.jpg / .png',
    'Foto sesi tanya jawab atau pelatihan penggunaan dashboard SITRIA (8 April 2026)',
    'Foto landscape (4:3 atau 16:9)')

img_placeholder(doc, '5.3',
    'screenshot_sitria_live.png',
    'Screenshot sistem SITRIA yang sudah aktif di server Lab Inovasi Digital (15 April 2026)',
    'Screenshot browser dengan URL server terlihat, landscape (16:9)')

img_placeholder(doc, '5.4',
    'daftar_hadir_sosialisasi.jpg / .png',
    'Scan atau foto daftar hadir peserta sosialisasi (23 peserta, 7–8 April 2026)',
    'Foto dokumen A4 yang sudah ditandatangani peserta, portrait')

img_placeholder(doc, '5.5',
    'hasil_evaluasi_kuesioner.png',
    'Screenshot atau rekap grafik hasil kuesioner evaluasi kepuasan pengguna (rata-rata 4,3/5,0)',
    'Screenshot grafik/tabel hasil kuesioner, landscape')

# ═══════════════════════════════════════════════

output_path = r'd:\Github-ADL\presentasi-umum\CPNS\laporan-progress\Laporan_Akhir_Aktualisasi_SITRIA_2026.docx'
doc.save(output_path)
print(f'[OK] Laporan akhir berhasil dibuat: {output_path}')
