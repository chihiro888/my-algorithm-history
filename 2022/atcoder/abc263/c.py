from itertools import *

n, m = map(int, input().split())

x = []
for d in range(1, m+1):
    x.append(d)

pList = list(permutations(x, n))

solve = []
for p in pList:
    p = list(p)
    is_sorted = all(p[i] < p[i+1] for i in range(len(p)-1))
    if (is_sorted):
        solve.append(p)
        result = ' '.join(str(s) for s in p)
        print(result)