import time
from tqdm import tqdm

print("Starting Vending Machine")

time.sleep(2)

for i in tqdm (range (250), 
			desc="Loading…", 
			ascii=False, ncols=75):
	time.sleep(0.01)
	
print("Vending Machine ala Tjiani is Ready!")

a = int(input("Masukan jumlah transaksi: "))

for i in range(a):
    print(f"\nTransaksi ke - {i + 1}")
    time.sleep(1)

    print("\nDaftar Barang:")
    print("1. Kopi (Rp 80,000)")
    print("2. Ciki (Rp 10,000)")
    print("3. Xiaomi 14 ULTRA (Rp 42,000,000)")
    
    item = int(input("Masukan nomor barang yang ingin dibeli: "))
    
    if item == 1:
        harga = 80000
        nama_barang = "Kopi"
    elif item == 2:
        harga = 10000
        nama_barang = "Ciki"
    elif item == 3:
        harga = 42000000
        nama_barang = "Xiaomi 14 ULTRA"
    else:
        print("Barang tidak tersedia!")
        continue
    
    print(f"\nAnda memilih {nama_barang} dengan harga Rp {harga:,}")
    
    duit = int(input("Masukan uang: "))
    
    a1 = int(input("Koin 100: "))
    a2 = int(input("Koin 500: "))
    a3 = int(input("Koin 1000: "))
    a4 = int(input("Lembaran 1000: "))
    a10 = a3 + a4
    a5 = int(input("Lembaran 5000: "))
    a6 = int(input("Lembaran 10.000: "))
    a7 = int(input("Lembaran 20.000: "))
    a8 = int(input("Lembaran 50.000: "))
    a9 = int(input("Lembaran 100.000: "))
    
    total = (a1*100)+(a2*500)+(a10*1000)+(a5*5000)+(a6*10000)+(a7*20000)+(a8*50000)+(a9*100000)
    
    time.sleep(2)


    for i in tqdm (range (250), 
                desc="Memproses", 
                ascii=False, ncols=75):
        time.sleep(0.01)
        
    print("")

	
    
    
    if total >= harga:
        kembalian = total - harga
        print(f"Pembayaran berhasil! Anda membeli {nama_barang} seharga Rp {harga:,}")
        print(f"Total uang anda: Rp {total:,}")
        print(f"Kembalian: Rp {kembalian:,}")
    else:
        kurang = harga - total
        print(f"Uang anda kurang Rp {kurang:,}! Pembayaran gagal.")
