# 1 <= n <= 100000
n = int(input())
d = []
d.append(0)
for _ in range(n):
    d.append(int(input()))

print(f'd = {d}')
k = d[1] # 4
for i in range(1, len(d)):
    x = k - d[i-1] # 4 - 0, 3 - 4
    if x > 0:
        k = d[i] # 4
    
    print(f'x = {x}')