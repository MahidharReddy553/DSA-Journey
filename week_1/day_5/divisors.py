n = 45
d = []
for i in range(1, n + 1):
    if n % i == 0:
        d.append(i)

print('All divisors of the number :', n)
print(d)