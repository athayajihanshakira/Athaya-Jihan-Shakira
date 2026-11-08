class pengguna:
    
    def __init__(self, nama_depan, nama_belakang, umur, alamat):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.umur = umur
        self.alamat = alamat
        self.percobaan_login = 0

    def jelaskan_pengguna(self):
        print(f"Pengguna: {self.nama_depan} {self.nama_belakang}")
        print(f"Umur: {self.umur} tahun, alamat: {self.alamat}")

    def penambahan_percobaan_login(self):
        self.percobaan_login += 1

    def hapus_percobaan_login(self):
        self.percobaan_login = 0

pengguna_1 = pengguna ("Budi", "Santoso", "20", "amerika")
pengguna_1.jelaskan_pengguna()
pengguna_1.penambahan_percobaan_login()
pengguna_1.penambahan_percobaan_login()
pengguna_1.penambahan_percobaan_login()

print(f"Jumlah percobaan login: {pengguna_1.percobaan_login}")
pengguna_1.hapus_percobaan_login()
print(f"Jumlah percobaan login setelah direset: {pengguna_1.percobaan_login}")