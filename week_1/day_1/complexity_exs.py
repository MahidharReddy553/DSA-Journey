def constant(arr):
    return arr[0]

def linear(arr):
    for i in arr:
        print(i)

def quadratic(arr):
    for i in arr:
        for j in arr:
            print(i, j)


arr = [1,2,3,4,5,6]


print(constant(arr))

linear(arr)

quadratic(arr)