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
    d = int(ip())
    r = int(d / 4)
    s = ''
    for _ in range(r):
        s += 'long '
    s += 'int'
    print(s)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------