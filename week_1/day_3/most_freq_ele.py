arr = [1, 2, 2, 3, 2]

freq = {}

for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

sort_freq = sorted(freq.items(), key = lambda x : -x[1])
print(sort_freq[0][0], 'occured', sort_freq[0][1], 'times')