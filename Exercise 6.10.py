angka_favorit = {
    'andi': [7, 14],
    'siti': [12, 5, 9],
    'eko': [3],
    'rina': [9, 21, 33],
    'joko': [5, 10],
}

for nama, angka_list in angka_favorit.items():
    print(f"\nAngka favorit {nama.title()} adalah:")
    for angka in angka_list:
        print(f"- {angka}")