n = 1221
nc = n
rn = 0
while n != 0:
    c = n % 10
    rn = rn * 10 + c
    n = n // 10
print("reveresed number is:", rn)

if rn == nc:
    print(f"{nc} is a palindrome")
else:
    print(f"{nc} is not a palindrome")