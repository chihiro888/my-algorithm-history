n = int(input())
d = []
for _ in range(n):
    d.append(list(map(int, input().split())))
    
for i in range(1, len(d)):
    for j in range(i+1):
        if j == 0:
            d[i][j] += d[i-1][j]
        elif j == i:
            d[i][j] += d[i-1][j-1]
        else:
            d[i][j] += max(d[i-1][j], d[i-1][j-1])

print(max(d[-1]))