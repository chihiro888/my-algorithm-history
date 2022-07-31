n, m = map(int, input().split())
adjs = [set() for i in range(n+1)]
cnt = 0

for i in range(m):
    a, b = map(int, input().split())
    adjs[a].add(b) if a < b else adjs[b].add(a)

for sets in adjs:
    for i in sets:
        cnt += len(sets.intersection(adjs[i]))

print(cnt)