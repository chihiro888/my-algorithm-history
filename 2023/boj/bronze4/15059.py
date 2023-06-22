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
    a, b, c = mv(int)
    x, y, z = mv(int)

    d = []
    if z - c > 0:
        d.append(z - c)
    if y - b > 0:
        d.append(y - b)
    if x - a > 0:
        d.append(x - a)
    
    print(sum(d))
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------