
def natural_s(n):
    if n == 0:
        return 0
    return n + natural_s(n - 1)
    
print(natural_s(6))