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
    s = ip()
    x = s.split('/')
    k = int(x[0])
    d = int(x[1])
    a = int(x[2])
    if k + a < d or d == 0:
        print('hasu')
    else:
        print('gosu')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------