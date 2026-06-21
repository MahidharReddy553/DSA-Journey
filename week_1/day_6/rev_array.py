def rev_arr(arr, l, r):
    arr[l], arr[r] = arr[r], arr[l]
    l += 1
    r -= 1
    if l >= r:
        return arr
    return rev_arr(arr, l, r)

arr = [3,4,5,6]
print(rev_arr(arr, 0, len(arr) - 1))