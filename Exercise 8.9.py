def tampilkan_pesan(daftar_pesan):
    """Mencetak setiap pesan yang ada di dalam list."""
    for pesan in daftar_pesan:
        print(pesan)

pesan_singkat = [
    "Halo, apa kabar?", 
    "Jangan lupa belajar Python ya.", 
    "Semoga harimu menyenangkan!"
]

tampilkan_pesan(pesan_singkat)