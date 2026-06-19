n1 = 105
n2 = 252

while n2!=0:
    n1, n2 = n2, n1 % n2
    
print(n1)