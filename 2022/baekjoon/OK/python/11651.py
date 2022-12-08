n = int(input())

d = []
for _ in range(n):
    d.append(list(map(int, input().split())))

d = sorted(d, key=lambda x : (x[1], x[0]) )

for x in d:
    print(f'{x[0]} {x[1]}')