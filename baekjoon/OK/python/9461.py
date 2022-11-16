dp = [0 for _ in range(100)]
dp[0] = 1
dp[1] = 1
dp[2] = 1

for i in range(3, 100):
    dp[i] = dp[i-3] + dp[i-2]
    
# print(f'dp = {dp}')

n = int(input())
for _ in range(n):
    x = int(input())    
    print(f'{dp[x-1]}')
    
    
