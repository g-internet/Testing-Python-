import random

a = (random.randint(0,220))
b = (random.randint(0,500))

if a > 10:
    print("a lebih besar dri pada 10")
elif a == 10:
    print("a sama dengan 10")
elif a == b:
    print("a sama dengan", a ,"|" , b)
else:
    print("a lebih kecil dri 10")