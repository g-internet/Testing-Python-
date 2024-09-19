import time
print("selamat datang di bisokop")

harga_tiket_anak = 30000
harga_tiket_dewasa = 50000
harga_tiket_lansia = 35000

penonton = int(input("jumlah penonton: "))


for i in range(penonton):
    tiket_anak = int(input("masukan jumlah tiket anak: "))
    tiket_dewasa = int(input("masukan jumlah tiket dewasa: "))
    tiket_lansia = int(input("masukan jumlah tiket lansia: "))
    total_harga_tiket = (tiket_anak * harga_tiket_anak) + (tiket_dewasa * harga_tiket_dewasa) + (tiket_lansia * harga_tiket_lansia)
    print(f"kamu membeli tiket anak sebanyak {tiket_anak} dengan harga {harga_tiket_anak} , tiket dewasa sebanyak {tiket_dewasa} dengan harga {harga_tiket_dewasa}, tiket lansia sebanyak {tiket_lansia} dengan harga {harga_tiket_lansia}")
    print(f"total kamu membeli itu {total_harga_tiket}")