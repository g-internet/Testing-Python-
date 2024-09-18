arga = int(input("masukan jumlah pelanggan"))

for i in range(arga):
    jumlah_barang = int(input("masukan jumlah barang: "))

    nama_barang = (input("masukan nama barang: "))
    harga_barang = float(input("masukan harga barang: "))

    total_pembelian = harga_barang

pajak = total_pembelian *0.1

total = total_pembelian + pajak

print(f"total harga sebelum pajak adalah {total_pembelian} , total harga setelah pajak 10% adalah {total}")