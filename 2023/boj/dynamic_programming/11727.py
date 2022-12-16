import sys


# Utilities ---------------------
debug = True
def p(name, value):
    if debug: print(f'{name} = {value}')
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
# -------------------------------


# Function Block ----------------

# -------------------------------


# Please write the code below ---
def main():
    n = int(ip())

    dp = [0] * 1001
    dp[1] = 1
    dp[2] = 3
    # dp[3] = 5
    # dp[4] = 11
    # dp[5] = 21

    for i in range(3, 1001):
        dp[i] = (dp[i-2] * 2) + dp[i-1]

    print(dp[n] % 10007)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------
