glosarium = {
    'dictionary': 'Kumpulan pasangan key-value (kunci-nilai) dalam Python.',
    'string': 'Deretan karakter yang diapit oleh tanda kutip.',
    'conditional test': 'Pengujian logika yang menghasilkan nilai True atau False.',
    'loop': 'Perulangan untuk menjalankan blok kode secara berulang-ulang.',
    'list': 'Kumpulan item yang berurutan dan dapat diubah (mutable).',
    'set': 'Kumpulan item unik tanpa duplikat yang tidak berurutan.',
    'tuple': 'Kumpulan item yang sifatnya tetap (immutable) dan tidak dapat diubah.',
    'float': 'Tipe data angka desimal (pecahan).',
    'integer': 'Tipe data angka bulat.',
    'boolean': 'Tipe data yang hanya bernilai True atau False.'
}

for kata, arti in glosarium.items():
    print(f"\n{kata.title()}:")
    print(f"\t{arti}")