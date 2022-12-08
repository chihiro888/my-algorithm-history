def dp(i, memo):
    a = 99999999
    b = 99999999
    c = 99999999

    # case 1
    n = int(i-1)
    c = memo[n] + 1

    # case 2
    if i % 3 == 0:
        n = int(i/3)
        a = memo[n] + 1
    # case 3
    if i % 2 == 0:
        n = int(i/2)
        b = memo[n] + 1

    memo[i] = min(a, b, c)

def main():
    # 1 <= n <= 1000000
    n = int(input())

    memo = [0 for _ in range(n+1)]

    for i in range(2, n+1):
        dp(i, memo)
    
    print(memo[n])

if __name__ == "__main__":
    main()