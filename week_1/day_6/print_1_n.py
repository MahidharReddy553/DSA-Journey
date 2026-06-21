def print_1_n(c, n):
    if c > n:
        return
    print(c)
    print_1_n(c + 1, n)

print_1_n(1, 6)