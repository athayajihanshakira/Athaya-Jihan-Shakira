glosarium = {
    'dictionary': 'Kumpulan pasangan key-value (kunci-nilai) dalam Python.',
    'string': 'Deretan karakter yang diapit oleh tanda kutip.',
    'conditional test': 'Pengujian logika yang menghasilkan nilai True atau False.',
    'loop': 'Perulangan untuk menjalankan blok kode secara berulang-ulang.',
    'list': 'Kumpulan item yang berurutan dan dapat diubah (mutable).'
}

# Mencetak setiap kata dan artinya dengan format yang rapi
for kata, arti in glosarium.items():
    print(f"\n{kata.title()}:")
    print(f"\t{arti}")