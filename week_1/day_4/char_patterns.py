
def chr_tri(n):
    ch = ord('A')
    for i in range(n):
        for j in range(i+1):
            print(chr(ch + j), end = ' ')
        print()
        
# chr_tri(5)

def r_chr_tri(n):
    ch = ord('A')
    for i in range(n):
        for j in range(n - i):
            print(chr(ch + j), end = ' ')
        print()

# r_chr_tri(5)

def chr_tri1(n):
    ch = ord('A')
    for i in range(n):
        for j in range(i + 1):
            print(chr(ch + i), end = ' ')
        print()

# chr_tri1(5)

def chr_rev(n):
    ch = ord('A') + n - 1
    for i in range(n):
        for j in range(i + 1):
            print(chr(ch + j), end = ' ')
        ch -= 1
        print()

# chr_rev(7)


def alpha_hill_tri(n):
    
    for i in range(n):
        for j in range(n - i):
            print(' ', end=' ')

        p = (i*2+1)//2
        ch = ord('A')
        
        for j in range(i * 2 + 1):
            print(chr(ch), end = ' ')
            if j < p:
                ch += 1
            else:
                ch -= 1         
        print()

alpha_hill_tri(5)