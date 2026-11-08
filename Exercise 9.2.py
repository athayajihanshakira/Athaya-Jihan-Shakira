class Restoran :
    def __init__ (self, nama_restoran, jenis_restoran):
        self.nama_restoran = nama_restoran
        self.jenis_restoran = jenis_restoran

    def deskripsi_restoran (self):
        print (f"restoran bernama {self.nama_restoran} memiliki jenis {self.jenis_restoran}")

restoran_1 = Restoran ("sederhana", "masakan padang")
restoran_2 = Restoran ("Enak", "seafood")
restoran_3 = Restoran ("mantap", "makanan cina")

restoran_1.deskripsi_restoran()
restoran_2.deskripsi_restoran()
restoran_3.deskripsi_restoran()
