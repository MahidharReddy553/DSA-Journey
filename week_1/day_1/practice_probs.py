def lar_ele(arr):
    return max(arr)

def sum_arr(arr):
    return sum(arr)

def c_even(arr):
    c = 0
    for i in arr:
        if i % 2 == 0:
            c += 1
    return c

arr = [10, 20, 30, 40, 50]


print(lar_ele(arr))
print(sum_arr(arr))
print(c_even(arr))