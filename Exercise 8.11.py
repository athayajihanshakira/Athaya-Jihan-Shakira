def kirim_pesan(daftar_pesan, pesan_terkirim):
    """Mencetak setiap pesan dan memindahkannya ke list pesan_terkirim."""
    while daftar_pesan:
        pesan_sekarang = daftar_pesan.pop(0)
        print(f"Mengirim pesan: {pesan_sekarang}")
        pesan_terkirim.append(pesan_sekarang)

# List awal
daftar_pesan_asli = [
    "Halo, apa kabar?", 
    "Jangan lupa belajar Python ya.", 
    "Semoga harimu menyenangkan!"
]
pesan_terkirim = []

kirim_pesan(daftar_pesan_asli[:], pesan_terkirim)

print("\n--- Status List Setelah Menggunakan Slice [:] ---")
print(f"List Asli (daftar_pesan_asli): {daftar_pesan_asli}")
print(f"List Terkirim (pesan_terkirim): {pesan_terkirim}")