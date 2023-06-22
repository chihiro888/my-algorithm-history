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
    a = int(ip())
    b = int(ip())
    c = int(ip())
    d = int(ip())
    e = int(ip())
    f = int(ip())

    x = (a*3)+(b*2)+(c)
    y = (d*3)+(e*2)+(f)

    if x > y:
        print('A')
    elif x == y:
        print('T')
    else:
        print('B')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------