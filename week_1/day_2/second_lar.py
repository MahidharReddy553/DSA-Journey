li = [7, 45, 69, 1, 46, 63, 3, 333]
nli = list(set(li))
me = nli[0]
sle = li[0]

for i in nli:
    if i > me:
        sle = me
        me = i
    elif i != me and i > sle:
        sle = i

print('largest :', me)
print('second largest:', sle)