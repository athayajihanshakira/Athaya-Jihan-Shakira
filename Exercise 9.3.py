class pengguna :
    def __init__ (self, nama_depan, nama_belakang, umur, alamat) :
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.umur = umur
        self.alamat = alamat

    def deskripsi_pengguna (self) :
        print (f"nama: {self.nama_depan} {self.nama_belakang}")
        print (f"umur: {self.umur}")
        print (f"alamat: {self.alamat}")
    def sapa_pengguna (self) :
        print (f"selamat datang {self.nama_depan}!!")

pengguna_1 = pengguna ("athaya", "azizah", "13", "london")
pengguna_2 = pengguna ("azkiya", "nurul", "15", "indonesia")

pengguna_1.deskripsi_pengguna()
pengguna_1.sapa_pengguna()
pengguna_2.deskripsi_pengguna()
pengguna_2.sapa_pengguna()