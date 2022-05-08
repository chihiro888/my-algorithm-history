# 1 <= n <= 200000
n = int(input())

# -1000000000 <= a[i], b[i] <= 1000000000
# 1 <= i <= n
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# print(f'n = {n}')
# print(f'a = {a}')
# print(f'b = {b}')

minData = None
# 200000 -> O(N)
for l in range(1, n+1):
    # 200000 -> O(N)
    for r in range(1, n+1):
        if l <= r:
            # print(f'({l}, {r})')
            x = max(a[l-1:r])
            y = min(b[l-1:r])
            # print(f'x = {x}, y = {y}')
            d = x * y
            # print(f'd = {d}')
            if minData == None or minData >= d:
                minData = d
                
# print(f'minData = {minData}')
print(minData)


# O(N) x O(N) = O(N^2)