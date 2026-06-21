def fibo(n):
    if n < 1:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    return fibo(n - 1) + fibo(n - 2)

print(fibo(5))

# for i in range(1, 6):
#     print(fibo(i))