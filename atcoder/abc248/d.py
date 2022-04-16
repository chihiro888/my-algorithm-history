# 5
N = int(input())

# [3, 1, 4, 1, 5]
A = list(map(int, input().split()))

# 4
Q = int(input())

for _ in range(Q):
    # 1, 5, 1
    l, r, x = map(int, input().split())
    
    # solve
    print(A[l-1:r].count(x))
    