import random

a =(random.randint(0,8)) 
b =(random.randint(0,8))
c =(random.randint(0,8))


if a > b and a > c:
    print("A common")
elif  b > a and b > c:
    print("b Rare")
elif  c > a and c > b:
    print("C LEGENDARY")
else:
    print("ZONK")