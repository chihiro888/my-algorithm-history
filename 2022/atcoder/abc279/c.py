h, w = map(int, input().split())

s = []
t = []
for _ in range(h):
    s.append([x for x in input()])
for _ in range(h-1, (h*2)-1):
    t.append([x for x in input()])

solve = 'Yes'
idx = 0
for _ in range(h):
    if s[idx].count('#') != t[idx].count('#'):
        solve = 'No'
        break
    idx += 1

print(solve)