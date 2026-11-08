class Restoran :
    def __init__ (self, nama_restoran, jenis_restoran):
        self.nama_restoran = nama_restoran
        self.jenis_restoran = jenis_restoran

    def deskripsi_restoran (self):
        print (f"restoran bernama {self.nama_restoran} memiliki jenis {self.jenis_restoran}")
    def buka_restoran (self):
        print (f"restoran {self.nama_restoran} sedang dibuka")

restoran_favorit = Restoran ("sederhana", "masakan_padang")
print (restoran_favorit.nama_restoran)
print (restoran_favorit.jenis_restoran)

restoran_favorit.deskripsi_restoran()
restoran_favorit.buka_restoran()