n, m = map(int, input().split())
adj = [set() for i in range(n+1)]
solve = 0

for i in range(m):
    a, b = map(int, input().split())
    if a < b:
        adj[a].add(b)
    else:
        adj[b].add(a)

for sets in adj:
    for i in sets:
        solve += len(sets.intersection(adj[i]))

print(solve)
