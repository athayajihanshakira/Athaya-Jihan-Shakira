bahasa_pemrograman = ["Python", "Java", "C++", "JavaScript", "Ruby"]
print("List awal:", bahasa_pemrograman)

print(f"Bahasa pertama yang dipelajari adalah {bahasa_pemrograman[0]}.")

bahasa_pemrograman[2] = "C#"
print("Setelah diubah (C++ jadi C#):", bahasa_pemrograman)

bahasa_pemrograman.append("Go")
print("Setelah append:", bahasa_pemrograman)

bahasa_pemrograman.insert(1, "TypeScript")
print("Setelah insert:", bahasa_pemrograman)

del bahasa_pemrograman[0]
print("Setelah del indeks 0:", bahasa_pemrograman)

bahasa_terhapus = bahasa_pemrograman.pop()
print(f"Bahasa yang dihapus dengan pop: {bahasa_terhapus}")
print("List setelah pop:", bahasa_pemrograman)

print("Urutan alfabet sementara:", sorted(bahasa_pemrograman))

bahasa_pemrograman.reverse()
print("Setelah dibalik (reverse):", bahasa_pemrograman)

bahasa_pemrograman.sort()
print("Setelah disortir permanen (sort):", bahasa_pemrograman)
print(f"Jumlah total bahasa yang tersisa ada {len(bahasa_pemrograman)} buah.")