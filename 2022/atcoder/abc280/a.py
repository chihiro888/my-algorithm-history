n, m = map(int, input().split())

s = 0
for _ in range(n):
    d = [x for x in input()]
    s += d.count('#')

print(s)