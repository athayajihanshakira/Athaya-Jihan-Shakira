favorite_places = {
    'budi': ['bali', 'yogyakarta', 'lombok'],
    'siti': ['bandung', 'malang'],
    'joko': ['raja ampat', 'bunaken', 'bromo'],
}

for nama, tempat_list in favorite_places.items():
    print(f"\nTempat favorit {nama.title()} adalah:")
    for tempat in tempat_list:
        print(f"- {tempat.title()}")