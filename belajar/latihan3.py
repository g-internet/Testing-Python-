# Fungsi untuk menghitung diskon berdasarkan kategori barang
def hitung_diskon(kategori, harga):
    if kategori == "Elektronik":
        return harga * 0.05  # Diskon 5% untuk Elektronik
    elif kategori == "Pakaian":
        return harga * 0.10  # Diskon 10% untuk Pakaian
    elif kategori == "Makanan":
        return harga * 0.03  # Diskon 3% untuk Makanan
    else:
        return 0  # Tidak ada diskon untuk kategori lain

# Fungsi untuk menghitung harga setelah diskon
def hitung_harga_diskon(harga, diskon):
    return harga - diskon

# Input jumlah barang yang ingin dibeli
jumlah_barang = int(input("Masukkan jumlah barang yang ingin dibeli: "))

total_belanja = 0
total_diskon = 0

for i in range(jumlah_barang):
    print(f"\nBarang ke-{i+1}")
    nama_barang = input("Masukkan nama barang: ")
    harga = float(input("Masukkan harga barang: "))
    kategori = input("Masukkan kategori barang (Elektronik, Pakaian, Makanan): ").capitalize()

    # Hitung diskon dan harga setelah diskon
    diskon = hitung_diskon(kategori, harga)
    harga_diskon = hitung_harga_diskon(harga, diskon)

    print(f"Diskon untuk {nama_barang}: Rp {diskon:.2f}")
    print(f"Harga setelah diskon: Rp {harga_diskon:.2f}")

    # Tambahkan ke total belanja dan total diskon
    total_belanja += harga
    total_diskon += diskon

# Tampilkan total belanja, diskon, dan harga setelah diskon
print(f"\nTotal belanja: Rp {total_belanja:.2f}")
print(f"Total diskon: Rp {total_diskon:.2f}")
print(f"Total harga setelah diskon: Rp {total_belanja - total_diskon:.2f}")
