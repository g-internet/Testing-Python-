a = int(input("Masukkan jumlah pasien"))
for i in range (a):
    nama = (input("Masukkan nama pasien"))
    berat_badan = float(input("Masukkan berat badan pasien"))
    tinggi_badan = float(input("Masukkan tinggi badan pasien"))
    
    bmi = berat_badan/tinggi_badan
    
    if bmi < 18.5:
        print("Kamu terlalu keras")
    elif bmi > 18.6 and bmi < 25.9:
        print("Berat badan kamu normal")
    elif bmi > 26 and bmi < 29.9:
        print("Kamu terlalu gendut")
    else:
        print("Kamu obesitas")           
        
        