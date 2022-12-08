k = int(input())
d = []
for _ in range(k):
    x = int(input())
    if x == 0:
        d.pop()
    else:
        d.append(x)
print(sum(d))