class Pengguna:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def tampilkan_pengguna(self) :
        print (f"nama : {self.nama}")
        print (f"umur ; {self.umur}")

class HakIstimewa:
    def __init__(self):
        self.daftar_hak = [
            "Dapat menambahkan postingan",
            "Dapat menghapus postingan",
            "Dapat memblokir pengguna"
        ]

    def tampilkan_hak(self):
        print("Hak istimewa admin:")
        for hak in self.daftar_hak:
            print(f"- {hak}")

class Admin(Pengguna):
    def __init__(self, nama, umur):
        super().__init__(nama, umur)
        self.hak_istimewa = HakIstimewa()

admin1 = Admin("Athaya", 19)
admin1.tampilkan_pengguna()
admin1.hak_istimewa.tampilkan_hak()