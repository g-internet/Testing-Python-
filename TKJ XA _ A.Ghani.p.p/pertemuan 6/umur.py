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
time.sleep(2)
from tqdm import tqdm
import time


for i in tqdm (range (250), 
			desc="Loading…", 
			ascii=False, ncols=75):
	time.sleep(0.01)
	
print("Complete.")


if umur < 13:
    print("umur anda dibawah 13 tahun, anda dilarang masuk")
elif umur >= 13 and umur < 32 :
    print("umur anda sudah diatas 13, silakan masuk")
elif umur >= 32 and umur < 60 :
    print("umur anda sudah dewasa Sudah jelas Boleh  silakan masuk")
elif umur >= 60 and umur < 100 :
    print("umur anda sudah menujukan bahwa anda sudah bau tanah silakang pulang")
