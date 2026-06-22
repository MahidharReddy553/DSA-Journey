arr = [1,2,3,4,2,1,4,5,6,3,1,2,4,6]

freqs = {}

for i in arr:
    if i in freqs:
        freqs[i] += 1
    else:
        freqs[i] = 1

print(freqs)