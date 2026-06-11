li = [7, 45, 69, 1, 46, 63, 3]
# li.sort()
is_sorted = True

e = li[0]
for i in range(1, len(li)-1):
    if e > li[i]:
        is_sorted = False
        break

print(is_sorted)