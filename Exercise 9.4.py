class Restoran :
    def __init__ (self, nama_restoran, jenis_restoran):
        self.nama_restoran = nama_restoran
        self.jenis_restoran = jenis_restoran
        self.jumlah_pelanggan = 0

    def deskripsi_restoran (self):
        print (f"restoran bernama {self.nama_restoran} memiliki jenis {self.jenis_restoran}")
    def buka_restoran (self):
        print (f"restoran {self.nama_restoran} sedang dibuka")
    def pelanggan_awal (self) :
        print (f"pelanggan yang dilayani {self.jumlah_pelanggan}")
    def atur_pelanggan (self, perubahan_pelanggan) :
        self.jumlah_pelanggan = perubahan_pelanggan
    def tambahan_pelanggan (self, jumlah_tambahan) :
        self.jumlah_pelanggan += jumlah_tambahan

restoran_favorit = Restoran ("sederhana", "masakan_padang")

restoran_favorit.deskripsi_restoran()
restoran_favorit.buka_restoran()
restoran_favorit.pelanggan_awal()
restoran_favorit.atur_pelanggan(50)
restoran_favorit.pelanggan_awal()
restoran_favorit.tambahan_pelanggan(25)
restoran_favorit.pelanggan_awal()
