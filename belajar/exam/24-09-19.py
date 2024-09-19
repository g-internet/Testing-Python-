print("Selamat datang di bioskop")

harga_tiket_anak = 30000
harga_tiket_dewasa = 50000
harga_tiket_lansia = 35000

penonton = int(input("Jumlah penonton: "))

for i in range(penonton):
    print(f"\nPenonton Ke {i+1}:")
    tiket_anak = int(input("Masukkan jumlah tiket anak (di bawah 12): "))
    tiket_dewasa = int(input("Masukkan jumlah tiket dewasa (12 - 60): "))
    tiket_lansia = int(input("Masukkan jumlah tiket lansia (diatas 60): "))

    total_harga_tiket = (tiket_anak * harga_tiket_anak) + (tiket_dewasa * harga_tiket_dewasa) + (tiket_lansia * harga_tiket_lansia)

    print(f"Kamu membeli tiket anak sebanyak {tiket_anak} dengan harga {harga_tiket_anak} per tiket,")
    print(f"tiket dewasa sebanyak {tiket_dewasa} dengan harga {harga_tiket_dewasa} per tiket,")
    print(f"tiket lansia sebanyak {tiket_lansia} dengan harga {harga_tiket_lansia} per tiket.")
    print(f"Total harga tiket yang kamu beli adalah Rp{total_harga_tiket}\n")
