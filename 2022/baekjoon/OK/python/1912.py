n = int(input())
d = list(map(int, input().split()))

for i in range(1, n):
    d[i] = max(d[i], d[i - 1] + d[i])
    
print(max(d))