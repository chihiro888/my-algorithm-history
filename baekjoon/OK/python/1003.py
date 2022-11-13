def main():
    dp = [[0, 0] for _ in range(50)]

    dp[0] = [1, 0]
    dp[1] = [0, 1]

    for i in range(2, 50):
        dp[i] = [
            dp[i-2][0] + dp[i-1][0], 
            dp[i-2][1] + dp[i-1][1]
        ]

    x = int(input())
    for _ in range(x):
        n = int(input())
        print(f'{dp[n][0]} {dp[n][1]}')

if __name__ == "__main__":
    main()