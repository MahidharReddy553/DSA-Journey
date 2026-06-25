arr = [9, 76, 46, 45, 26, 24]
# for i in range(len(arr)):
#     for j in range(len(arr) - i - 1):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
# print(arr)


def bubble_sort(arr,n = None):
    if n is None:
        n = len(arr)
    if n == 1:
        return arr
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i+1] = arr[i + 1], arr[i]

    return bubble_sort(arr, n - 1)

print(bubble_sort(arr))

