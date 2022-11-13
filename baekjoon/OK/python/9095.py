def main():
    dp = [0 for _ in range(12)]

    dp[1] = 1 # 1
    dp[2] = 2 # 1+1, 2
    dp[3] = 4 # 1+1+1, 1+2, 2+1, 3
    # dp[4] = 7 # 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1

    for i in range(4, 11):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    n = int(input())
    for _ in range(n):
        x = int(input())
        print(dp[x])

if __name__ == "__main__":
    main()