n = int(input())
a = list(map(int, input().split()))

solve = 0
for i in range(0, n):
    for j in range(i+1, n):
        if min(a[i], a[j]) == i+1:
            if max(a[i], a[j]) == j+1:
                solve += 1

print(solve)