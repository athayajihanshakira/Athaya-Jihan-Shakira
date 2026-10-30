makanan_favorit = "pizza"
print("Tes kesamaan string:", makanan_favorit == "pizza")          
print("Tes ketidaksamaan string:", makanan_favorit != "burger")    

nama_depan = "Budi"
print("Tes metode lower():", nama_depan.lower() == "budi")         

angka = 25
print("Tes sama dengan:", angka == 25)           
print("Tes tidak sama dengan:", angka != 30)     
print("Tes lebih besar dari:", angka > 20)      
print("Tes kurang dari:", angka < 50)            
print("Tes lebih besar/sama dengan:", angka >= 25)
print("Tes kurang/sama dengan:", angka <= 24)   

umur = 20
punya_izin = True
print("Tes keyword 'and':", umur >= 18 and punya_izin == True)

hari_ini = "sabtu"
print("Tes keyword 'or':", hari_ini == "sabtu" or hari_ini == "minggu") 

daftar_peserta = ["andi", "siti", "eko"]
print("Tes item ada di list ('in'):", "siti" in daftar_peserta)  

print("Tes item tidak di list ('not in'):", "joko" not in daftar_peserta)  