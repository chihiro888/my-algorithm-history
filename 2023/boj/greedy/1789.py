import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def find_maximum_N(S):
    N = 1
    while N * (N + 1) / 2 <= S:
        N += 1
    return N - 1
# -------------------------------


# Please write the code below ---
def main():
    n = int(ip())
    print(find_maximum_N(n))
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------