import random
from tqdm import tqdm
import time

num = int(input("Masukan nomor anda: "))
time.sleep(2)

num2 = int(input("Masukan perhitungan akhir anda: "))
time.sleep(2)

for i in tqdm(range(1000), desc="Loading…", ascii=True, ncols=75):
    time.sleep(0.0001)
    
print("Menampilkan hasil")

for i in range(num, num2):
    print(i)
