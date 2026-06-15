def square(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

# square(3)

def l_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            print('*', end = ' ')
        print()

# l_triangle(5)

def r_l_triangle(n):
    for i in range(n):
        for j in range(n - i):
            print('*', end = ' ')
        print()

# r_l_triangle(5)

def e_triangle(n):
    for i in range(n):
        for j in range(n - i + 1):
            print(' ', end = '')
        for j in range((i * 2) + 1):
            print('*', end = '')
        print()

# e_triangle(5)

def r_e_triangle(n):
    for i in range(n):
        for j in range(i):
            print(' ', end = '')
        for j in range(((n - i) * 2) - 1, 0, -1):
            print('*', end = '')
        print()

# r_e_triangle(5)

def diamond(n):
    for i in range(n):
        for j in range(n - i + 1):
            print(' ', end = '')
        for j in range((i * 2) + 1):
            print('*', end = '')
        print()

    for i in range(n):
        for j in range(i + 2):
            print(' ', end = '')
        for j in range(((n - i) * 2) - 1, 0, -1):
            print('*', end = '')
        print()

# diamond(5)

def s_triangle(n):
    for i in range(n):
        for j in range(i):
            print('*', end = '')
        print()
    for i in range(n):
        for j in range(n - i):
            print('*', end = '')
        print()

# s_triangle(5)

def h_diamond(n):
    for i in range(n):
        for j in range(n - i):
            print('*', end = '')
        for j in range((i * 2) + 1):
            print(' ', end = '')
        for j in range(n - i):
            print('*', end = '')
        print()

    for i in range(n):
        for j in range(i + 1):
            print('*', end = '')
        for j in range(((n - i) * 2) - 1, 0, -1):
            print(' ', end = '')
        for j in range(i + 1):
            print('*', end = '')
        print()

h_diamond(5)

def butterfly(n):
    for i in range(n):
        for j in range(i + 1):
            print('*', end='')
        for j in range((n - i) * 2 - 1):
            print(' ', end = '')
        for j in range(i + 1):
            print('*', end = '')
        print()
    for i in range(n):
        for j in range(n - i - 1):
            print('*', end = '')
        for j in range((i*2)+3):
            print(' ', end = '')
        for j in range(n - i - 1):
            print('*', end = '')
        print()
# butterfly(5)