import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def MenOfPassion(n):
    count = n * (n - 1) * (n - 2) // 6
    return count
# -------------------------------


# Please write the code below ---
def main():
    n = int(ip())
    print(MenOfPassion(n))
    print(3)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------