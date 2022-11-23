n = int(input())

d = []
dp = [0] * 3

for _ in range(n):
    d.append(list(map(int, input().split())))
    
for i in range(1, n):
    print(f'i = {i}')
    for j in range(3):
        print(f'j = {j}')
        if j == 0:
            dp[j] = dp[i-1][j] + max(dp[j], dp[j+1])
        elif j == 1:
            dp[j] = dp[i-1][j+1] + max(dp[j], dp[j+1], dp[j+2])
        elif j == 2:
            dp[j] = dp[i-1][j+2] + max(dp[j+1], dp[j+2])
            
        print(f'dp = {dp}')
    print('-----------------')