menu_prasmanan = ("nasi goreng", "mie ayam", "sate", "sop buah", "es teh")

print("Menu asli restoran:")
for makanan in menu_prasmanan:
    print(makanan)

# 2. Percobaan mengubah item secara langsung (ini akan memunculkan TypeError jika dijalankan)
# TypeError: 'tuple' object does not support item assignment
# menu_prasmanan[0] = "bubur ayam"  

menu_prasmanan = ("nasi goreng", "bakso", "sate", "jus alpukat", "es teh")

print("\nMenu revisi (setelah restoran memperbarui menu):")
for makanan in menu_prasmanan:
    print(makanan)