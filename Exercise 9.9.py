class Baterai:
    def __init__(self, kapasitas=50):
        self.kapasitas = kapasitas

    def tampilkan_jarak(self):
        jarak = self.kapasitas * 4
        print(f"Jarak tempuh mobil: {jarak} km")

    def tingkatkan_baterai(self):
        if self.kapasitas != 65:
            self.kapasitas = 65
            print("Kapasitas baterai berhasil ditingkatkan!")

class MobilListrik:
    def __init__(self, merek):
        self.merek = merek
        self.baterai = Baterai()

    def tampilkan_jarak(self):
        print(f"Mobil: {self.merek}")
        self.baterai.tampilkan_jarak()

mobil = MobilListrik("Tesla")

mobil.tampilkan_jarak()
mobil.baterai.tingkatkan_baterai()
mobil.tampilkan_jarak()