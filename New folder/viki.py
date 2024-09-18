a = int(input("Masukan jumlah pasien"))

for i in range (a):
    nama = (input("Masukkan nama pasien"))
    berat_badan = float(input("Masukkan berat badan anda"))
    tinggi_badan = float(input("Masukkan tinggi badan anda"))
    
    bmi = berat_badan / tinggi_badan
    
    if bmi < 18.5:
        print("Kamu terlalu kurus")
    elif bmi > 18.6 and bmi < 25.9:
        print("Berat badan kamu normal")
    elif bmi > 26 and bmi < 29.9:
        print("kamu gemuk")
    else:
        print("kamu obesitas")