orang_1 = {
    'nama_depan': 'budi',
    'nama_belakang': 'santoso',
    'usia': 25,
    'kota': 'jakarta',
}

orang_2 = {
    'nama_depan': 'siti',
    'nama_belakang': 'aminah',
    'usia': 22,
    'kota': 'bandung',
}

orang_3 = {
    'nama_depan': 'joko',
    'nama_belakang': 'widodo',
    'usia': 30,
    'kota': 'surabaya',
}

people = [orang_1, orang_2, orang_3]

for orang in people:
    nama_lengkap = f"{orang['nama_depan']} {orang['nama_belakang']}"
    print(f"\nNama Lengkap: {nama_lengkap.title()}")
    print(f"Usia: {orang['usia']}")
    print(f"Kota: {orang['kota'].title()}")