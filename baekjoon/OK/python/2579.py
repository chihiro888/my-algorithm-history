def main():
    d = [0] * 500
    n = int(input())
    for i in range(n):
        d[i] = int(input())

    dp = [0] * 500
    dp[0] = d[0]
    dp[1] = d[0] + d[1]
    dp[2] = max(d[0] + d[2], d[1] + d[2])

    for i in range(3, n):
        dp[i] = max(dp[i-3] + d[i-1] + d[i], dp[i-2] + d[i])

    print(dp[n-1])

if __name__ == "__main__":
    main()