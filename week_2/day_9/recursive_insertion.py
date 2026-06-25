arr = [92, 76, 46, 45, 26, 24]
for i in range(1, len(arr)):
    k = arr[i]
    j = i - 1
    while arr[j] > k and j>=0:
        arr[j+1] = arr[j]
        j -= 1
    arr[j + 1] = k
print(arr)


def insertion_sort(arr, i = 1):
    if i == len(arr):
        return arr
    k = arr[i]
    j = i - 1
    while j>=0 and arr[j] > k:
        arr[j+1] = arr[j]
        j -= 1
    arr[j + 1] = k
    insertion_sort(arr, i + 1)
    return arr


print(insertion_sort([92, 76, 46, 45, 26, 24]))