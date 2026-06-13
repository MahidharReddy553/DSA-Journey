### Counting occurrences of a target

arr = [1, 2, 2, 3, 2]
target = 2

freq = {}

for i in arr:
    if i == target:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

for i, j in freq.items():
    print("Number of times target occurred:", j)


def count_t_occuts(arr, target):
    tc = 0
    for i in arr:
        if i == target:
            tc += 1
    print(f"'{target}' occured {tc} times in the given array.")

count_t_occuts(arr, target)
