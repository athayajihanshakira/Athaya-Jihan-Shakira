class Restaurant:
    
    def __init__(self, nama_restoran, jenis_masakan):
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan

    def deskripsi_restoran(self):
        print(f"Restoran bernama {self.nama_restoran} menyajikan {self.jenis_masakan}.")

    def buka_restoran(self):
        print(f"Restoran {self.nama_restoran} sekarang sedang buka!")

class IceCreamStand(Restaurant):
    
    def __init__(self, nama_restoran, jenis_masakan="Es Krim"):
        super().__init__(nama_restoran, jenis_masakan)
        self.flavor = ["Cokelat", "Vanila", "Stroberi", "Mangga"]

    def tampilkan_rasa(self):
        print("Daftar rasa es krim yang tersedia:")
        for rasa in self.flavor:
            print(f"- {rasa}")

kios_es_krim = IceCreamStand("Es Krim Nikmat")
kios_es_krim.deskripsi_restoran()
kios_es_krim.buka_restoran()

print()
kios_es_krim.tampilkan_rasa()