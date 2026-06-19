n = 1634
nc = n
an = 0
c = 0
while nc != 0:
    c += 1
    nc //= 10
nc1 = n
while nc1 != 0:
    d = nc1 % 10
    an += d ** c
    nc1 //= 10

if n == an:
    print(f"{n} is an armstrog number")
else:
    print(f"{n} is not an armstrog number")