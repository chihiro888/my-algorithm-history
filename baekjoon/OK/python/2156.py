n = int(input())
d = [0] * 10000
for x in range(n):
    d[x] = int(input())
    
dp = [0] * 10000
dp[0] = d[0]
dp[1] = d[0] + d[1]
dp[2] = max(d[0]+d[2], d[1]+d[2], dp[1])

for i in range(3, n):
    dp[i] = max(d[i]+dp[i-2], d[i]+d[i-1]+dp[i-3], dp[i-1])
    
print(max(dp))