from itertools import combinations

n, k, d = map(int, input().split())
a = list(map(int, input().split()))

combs = list(combinations(a, k))

m = -1
for c in combs:
    s = sum(c)
    if s % d == 0:
        m = max(m, s)

print(m)