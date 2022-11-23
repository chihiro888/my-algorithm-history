d = []
for _ in range(28):
    d.append(int(input()))

s = 0
for i in range(1, 31):
    x = d.count(i)
    if x == 0:
        print(i)
        s += 1