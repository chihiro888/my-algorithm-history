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
    size = int(ip())
    t = []
    for _ in range(size):
        s, e = mv(int)
        t.append([s, e])

    t = sorted(t, key=lambda x: x[0])
    t = sorted(t, key=lambda x: x[1])

    l = 0
    c = 0
    for s, e in t:
        if s >= l:
            c += 1
            l = e

    print(c)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------