# 1 <= N <= 100,000
n = int(input())
# print(f'n = {n}')
d = []
for _ in range(n):
    # -100,000 <= xi, yi ≤ 100,000
    x, y = map(int, input().split())
    # print(f'x = {x}, y = {y}')
    d.append([x, y])

# print(d)
d = sorted(d , key=lambda k: [k[0], k[1]])
# print(d)
for i in d:
    print(f'{i[0]} {i[1]}')