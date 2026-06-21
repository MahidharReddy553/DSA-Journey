
def is_pali(s):
    sl = list(s)
    def rev(l, r):
        if l>=r:
            return
        sl[l], sl[r] = sl[r], sl[l]
        rev(l+1 , r-1)
    rev(0, len(sl) - 1)
    return list(s) == sl
print(is_pali('ama'))


def is_pali(s):
    def check(l, r):
        if l >= r:
            return True
        if s[l] != s[r]:
            return False
        return check(l+1, r-1)
    return check(0, len(s)-1)

print(is_pali('ama'))
print(is_pali('abc'))