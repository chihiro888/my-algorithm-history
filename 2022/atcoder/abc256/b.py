n = int(input())
a = list(map(int, input().split()))

x = []
for i in range(0, n):
    t = a[i]
    for j in range(i+1, n):
        t += a[j]
    x.append(t)

solve = 0
for k in x:
    if k > 3:
        solve += 1
        
print(solve)