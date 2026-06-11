li = [7, 45, 69, 1, 46, 63, 3]
target = 69
pos = None
for i in range(len(li)):
    if li[i] == target:
        pos = i
        break
print('Position of the element %d is at %s position'%(target, pos))