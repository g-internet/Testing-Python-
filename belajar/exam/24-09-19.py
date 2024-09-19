import time
from tqdm import tqdm

print("halo selamat datang di Penghitung Nilai Cepat")

time.sleep(2)
siswa = int(input("masukan jumlah siswa: "))
time.sleep(1)

print("isi data kamu dengan benar ya")

for i in range(siswa):
    
    nama_siswa = (input("masukan nama kamu!: "))
    
    tugas1 = float(input("masukan nilai tugas satu anda ya: "))
    tugas2 = float(input("masukan nilai tugas ke dua anda: "))
    tugas3 = float(input("masukan nilai tugas ke tiga anda: "))

    jumlah_nilai = tugas1 + tugas2 + tugas3

    nilai_rata = jumlah_nilai / 3
    
    if nilai_rata < 50:
        print(f"nilai rata-rata kamu itu {nilai_rata},maaf {nama_siswa} kamu belum lulus sabar ya!")
    elif nilai_rata >= 50 and nilai_rata < 70:
        print(f"nilai rata-rata kamu itu {nilai_rata}, waduh {nama_siswa} kalau kamu mau lulus kamu hrus ada perbaikan nilai dulu nih")
    else:
        print(f"nilai rata-rata kamu itu {nilai_rata}, Selamat ya {nama_siswa} Kamu sudah lulus")