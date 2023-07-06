import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------

# -------------------------------


# Please write the code below ---
def main():
    n = int(ip())
    dp = [0] * 100
    dp[0] = 0
    dp[1] = 1
    for i in range(0, 91):
        dp[i+2] = dp[i] + dp[i+1]

    print(dp[n])
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------