# 2 <= n <= 50
n = int(input())

# 1<= p < i (2 <= i <= n)
pList = list(map(int, input().split()))

print(max(pList))