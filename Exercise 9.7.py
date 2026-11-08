class Pengguna:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def deskripsi_pengguna(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")


class Admin(Pengguna):
    def __init__(self, nama, umur):
        super().__init__(nama, umur)
        self.hak_istimewa = [
            "Dapat menambahkan postingan",
            "Dapat menghapus postingan",
            "Dapat memblokir pengguna"
        ]

    def tampilkan_hak_istimewa(self):
        print("Hak istimewa admin:")
        for hak in self.hak_istimewa:
            print(f"- {hak}")


admin1 = Admin("Athaya", 19)
admin1.deskripsi_pengguna()
admin1.tampilkan_hak_istimewa()