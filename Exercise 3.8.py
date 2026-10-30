tempat_wisata = ["Jepang", "Swiss", "Kanada", "Korea Selatan", "inggris"]

print("Urutan Asli:")
print(tempat_wisata)

print("\nUrutan Alfabet (menggunakan sorted):")
print(sorted(tempat_wisata))

print("\nList setelah sorted (masih asli):")
print(tempat_wisata)

print("\nUrutan Alfabet Terbalik (Z-A):")
print(sorted(tempat_wisata, reverse=True))

print("\nList masih tetap asli:")
print(tempat_wisata)

tempat_wisata.reverse()
print("\nList setelah dibalik (reverse):")
print(tempat_wisata)

tempat_wisata.reverse()
print("\nList dikembalikan ke urutan asli:")
print(tempat_wisata)

tempat_wisata.sort()
print("\nList setelah disortir permanen (A-Z):")
print(tempat_wisata)

tempat_wisata.sort(reverse=True)
print("\nList setelah disortir permanen (Z-A):")
print(tempat_wisata)