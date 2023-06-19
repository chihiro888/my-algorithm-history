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
    x = int(ip())
    size = int(ip())
    t = 0
    for _ in range(size):
        d = ip().split(' ')
        t += (int(d[0]) * int(d[1]))
    if t == x:
        print('Yes')
    else:
        print('No')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------