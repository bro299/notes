import re
import json

with open("tulisan_saya.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Gabungkan semua menjadi 1 baris lalu split berdasar timestamp & nama
pattern = re.findall(r"\[(\d{1,2}/\d{1,2}/\d{4} \d{1,2}[:.]\d{2})] ([^:\n]+): (.*?)(?=\n\[\d{1,2}/|\Z)", content, re.DOTALL)

data = []
for dt, nama, pesan in pattern:
    nama = nama.strip()
    
    # Jika nama adalah nomor, tambahkan +62 jika belum ada
    if re.match(r"^\d{3,}", nama) and not nama.startswith("+62"):
        nama = f"+62 {nama}"

    # Bersihkan newline & spasi berlebih dalam pesan
    pesan = ' '.join(pesan.strip().split())

    data.append({
        "tanggal_waktu": dt.strip(),
        "nama": nama,
        "pesan": pesan
    })

with open("tulisan_structured_table.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Berhasil diproses ke tulisan_structured_table.json")
