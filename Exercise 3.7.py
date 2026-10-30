daftar_tamu = ["bila", "vika", "dela", "caca", "rara", "kila"]

print("Maaf sekali, meja baru tidak sempat datang, jadi saya hanya bisa mengundang dua orang.")

tamu_dihapus = daftar_tamu.pop()
print(f"Maaf {tamu_dihapus}, saya tidak bisa mengundang Anda ke makan malam.")

tamu_dihapus = daftar_tamu.pop()
print(f"Maaf {tamu_dihapus}, saya tidak bisa mengundang Anda ke makan malam.")

tamu_dihapus = daftar_tamu.pop()
print(f"Maaf {tamu_dihapus}, saya tidak bisa mengundang Anda ke makan malam.")

tamu_dihapus = daftar_tamu.pop()
print(f"Maaf {tamu_dihapus}, saya tidak bisa mengundang Anda ke makan malam.")

print(f"Halo {daftar_tamu[0]}, Anda masih diundang!")
print(f"Halo {daftar_tamu[1]}, Anda masih diundang!")

del daftar_tamu[0]
del daftar_tamu[0]

print("Daftar tamu saat ini:", daftar_tamu)