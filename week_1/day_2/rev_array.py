li = [7, 45, 69, 1, 46, 63, 3]
print('Before :', li)
l = 0
r = len(li) - 1

while l < r:
    li[l], li[r] = li[r], li[l]
    l += 1
    r -= 1

print('After :', li)