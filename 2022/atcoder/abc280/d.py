m = 23000
dp = [0] * m
dp[1] = 1
for i in range(2, m):
    dp[i] = dp[i-1] * i

k = int(input())

try:
    idx = 1
    while True:
        if dp[idx] % k == 0:
            print(idx)
            break
        idx += 1
except BaseException:
    print(k)