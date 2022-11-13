def main():
    max = 1000 + 1
    dp = [0 for _ in range(max)]

    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, max):
        dp[i] = dp[i-2] + dp[i-1]

    n = int(input())
    print(dp[n]%10007)

if __name__ == "__main__":
    main()