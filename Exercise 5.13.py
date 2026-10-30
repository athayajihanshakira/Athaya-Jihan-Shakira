usia_penonton = 18

if usia_penonton < 5:
    print(f"Usia {usia_penonton} tahun: Tiket GRATIS untuk balita!")
elif usia_penonton <= 12:
    print(f"Usia {usia_penonton} tahun: Kategori Anak-anak. Harga tiket diskon 50%.")
elif usia_penonton <= 59:
    print(f"Usia {usia_penonton} tahun: Kategori Dewasa. Harga tiket normal.")
else:
    print(f"Usia {usia_penonton} tahun: Kategori Lansia. Harga tiket spesial lansia (diskon khusus).")