a = True
b = False


print("ini yang and")
print(a and b)
print(a and a)
print(b and b)
print(b and a)
print("")
print("ini yang or")
print(a or b)
print(a or a)
print(b or b)
print(b or a)

print("")
print("ini yang Not")
print(not b)
print(not a)
print(not b)
print(not a)
print("")
print("")



# iseng cpu test


import time

time.sleep(5)

print("starting stres test")

from multiprocessing import Pool, cpu_count
from datetime import datetime

def stress_test(args):
    cpu, value = args
    start_time = datetime.now()
    for i in range(value):
        value = value * i
    print(f"cpu: {cpu} time: {datetime.now() - start_time}")

if __name__ == '__main__':
    start_time = datetime.now()
    cpu_count = cpu_count()
    with Pool(cpu_count) as mp_pool:
        mp_pool.map(stress_test, [(cpu, 100000000) for cpu in range(cpu_count)])
        mp_pool.map(stress_test, [(cpu, 100000000) for cpu in range(cpu_count)])
        mp_pool.map(stress_test, [(cpu, 100000000) for cpu in range(cpu_count)])
        mp_pool.map(stress_test, [(cpu, 100000000) for cpu in range(cpu_count)])
    print(f"total: {datetime.now() - start_time}")

time.sleep(20)




sheesh = ["land cruiser", "fortuner", "supra", "innova", "kijang", "alphard"]

print("Does the Kijang fit in the car, sheesh?", "kijang" in sheesh)
print("Does the Si Paling 2 GD exist?", "innova" in sheesh)
print("Surely there's no Nissan, right?", "nissan" in sheesh)
