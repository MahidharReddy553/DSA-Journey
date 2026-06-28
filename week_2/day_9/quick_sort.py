arr = [8, 4, 7, 9, 3, 10, 5]

def quick_sort(arr, l = 0, h = None):
    if h is None:
        h = len(arr) - 1

    if l < h:
        p = partition(arr, l, h)
        quick_sort(arr, l, p-1)
        quick_sort(arr, p+1, h)
        return arr

def partition(arr, l, h):
    p = arr[h]
    i = l - 1
    for j in range(l, h):
        if arr[j] <= p:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[h] = arr[h], arr[i + 1]
    return i + 1
print(quick_sort(arr))