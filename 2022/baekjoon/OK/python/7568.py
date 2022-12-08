# 2 <= N <= 50
n = int(input())
d = []
i = 0
for _ in range(n):
    # 10 <= x, y <= 200
    x, y = map(int, input().split())
    d.append([x, y])
    i += 1

for i in d:
    r = 1
    for j in d:
        if i[0] < j[0] and i[1] < j[1]:
                r += 1
    print(r, end=' ')