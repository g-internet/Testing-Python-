a = int(input("masukan jumlah pasien :")) 
for i in range (a):
    nama = input("masukan nama pasien :") 
    berat_badan = float(input("masukan berat badan pasien dalam kg :"))
    tinggi_badan = float(input("masukan tinggi badan pasien dalam meter :"))
    
    
    bmi = berat_badan / tinggi_badan
    print (bmi)
    
    if bmi < 18.5 :
        print("kamu kurus,perbanyak makan lagi ya")
    elif bmi >= 18.5 and bmi < 26 :
        print("kamu normal")
    elif bmi >= 26 and bmi < 30 :
        print("kamu kelebihan berat badan")
    else:
        print("kamu obesitas")
        
        