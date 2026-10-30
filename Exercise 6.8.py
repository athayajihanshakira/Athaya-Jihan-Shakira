peliharaan_1 = {
    'jenis_hewan': 'kucing',
    'nama_pemilik': 'ani',
}

peliharaan_2 = {
    'jenis_hewan': 'anjing',
    'nama_pemilik': 'budi',
}

peliharaan_3 = {
    'jenis_hewan': 'burung',
    'nama_pemilik': 'siti',
}

pets = [peliharaan_1, peliharaan_2, peliharaan_3]

for peliharaan in pets:
    print(f"\nInformasi Hewan Peliharaan:")
    print(f"- Jenis Hewan: {peliharaan['jenis_hewan'].title()}")
    print(f"- Pemilik: {peliharaan['nama_pemilik'].title()}")