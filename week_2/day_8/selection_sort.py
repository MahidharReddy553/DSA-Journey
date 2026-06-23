arr = [7,6,5,8,9,3,2,1,4]

for i in range(len(arr)):
    min_i = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_i]:
            min_i = j
    arr[i], arr[min_i] = arr[min_i], arr[i]

print(arr)