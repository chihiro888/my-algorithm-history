dp = [0] * 10000

def fibonacci(N):
    # use cache
    if dp[N] != 0:
        return dp[N]
    
    # main logic
    if N <= 1:
        return N
    else:
        dp[N] = fibonacci(N-1) + fibonacci(N-2)
        return dp[N]
        
def main():
    N = int(input())
    print(fibonacci(N))

if __name__ == "__main__":
    main()