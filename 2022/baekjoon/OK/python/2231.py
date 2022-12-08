st = {}
for n in range(0, 1000000):
    dSum = n + sum([int(char) for char in str(n)])
    if dSum not in st:
        st[dSum] = n

i = int(input())

if i in st:
    print(st[i])
else:
    print(0)