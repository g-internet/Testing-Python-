import random
import time
print(time)

print("halo selamat datang")
time.sleep(1)
print("silakan input nama dan umur anda")
time.sleep(2)

nama = (input("masukan nama anda"))

print("haloo apa kabar", nama)
time.sleep(2)

umur = int(input("masukan umur anda"))


print("sedang memproses Mohon di tunggu")

time.sleep(5)
print(("Getting Information"))
time.sleep(3)

if umur < 13:
    print("umur anda dibawah 13 tahun, anda dilarang masuk")
elif umur >= 13 and umur < 32 :
    print("umur anda sudah diatas 13, silakan masuk")
elif umur >= 32 and umur < 60 :
    print("umur anda sudah dewasa Sudah jelas Boleh  silakan masuk")
elif umur >= 60 and umur < 100 :
    print("umur anda sudah menujukan bahwa anda sudah bau tanah silakang pulang")
