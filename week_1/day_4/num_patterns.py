def num_triangle(n):
    for i in range(1, n+1):
        for j in range(i):
            print(i, end = '')
        print()

# num_triangle(5)

def num_triangle1(n):
    for i in range(1, n+1):
        for j in range(1,i+1):
            print(j, end = '')
        print()

# num_triangle1(5)

def rev_n_tri(n):
    for i in range(1, n+1):
        for j in range(1, n - i + 2):
            print(j, end = '')
        print()

# rev_n_tri(5)


def binary_tri(n):
    for i in range(n):
        if i % 2 == 0:
            s = 1
        else:
            s = 0
        for j in range(i + 1):
            print(s, end = '')
            if s == 0:
                s = 1
            else:
                s = 0
        print()

# binary_tri(5)

def n_butterfly(n):

    for i in range(1, n+1):
        for j in range(1,i+1):
            print(j , end = '')
        for j in range((n-i) * 2, 0, -1):
            print(' ', end = '')
        for j in range(i, 0, -1):
            print(j, end = '')
        print()


# n_butterfly(4)


def inc_tri(n):
    c = 1
    for i in range(n):
        for j in range(i+1):
            print(c, end = ' ')
            c += 1
        print()

# inc_tri(5)

