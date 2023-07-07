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
    n, m = mv(int)

    x = set()
    for _ in range(n):
        x.add(ip())

    y = set()
    for _ in range(m):
        y.add(ip())

    r = sorted(list(x & y))

    print(len(r))

    for i in r:
        print(i)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------