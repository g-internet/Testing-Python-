loop = int(input("masukan jumlah pelanggan"))

for i in range(loop):
    jumlah_barang = int(input("masukan jumlah barang"))
    total = 0
    for a in range(jumlah_barang):
        barang = (input("masukan nama barang"))
        harga_barang = int(input("masukan harga barang"))
        total += harga_barang
    print(f"total harga barang {total}")
    
    if total > 2000000:
        diskon = 0.2
    elif total > 1000000:
        diskon = 0.15
    elif total > 500000:
        diskon = 0.1
    else:
        diskon = 0
        
    jumlah_diskon = total * diskon
    jumlah_total = total - jumlah_diskon
    
    print(f"total belanja kamu itu {total}, dan kamu dapat diskon {jumlah_diskon}, total yang kamu harus bayar kan itu {jumlah_total}")