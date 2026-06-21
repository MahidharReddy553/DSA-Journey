
def n_print(n):
    if n==0:
        return
    print('Hi')
    n_print(n-1)

n_print(5)


def name_print(n):
    if n==0:
        return
    print('mahi '*n)
    name_print(n-1)

name_print(5)