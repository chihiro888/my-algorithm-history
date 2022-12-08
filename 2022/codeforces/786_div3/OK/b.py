import string 

# generate dictionary
a = string.ascii_lowercase
d = {}
idx = 1
for i in range(0, 26):
    for j in range(0, 26):
        if i != j:
            x = a[i] + a[j]
            d[x] = idx
            idx += 1

# 1 <= t <= 650
t = int(input())
for _ in range(t):
    s = input()
    print(d[s])