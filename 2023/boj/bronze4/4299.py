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
    s, m = mv(int)
    if  s+m < 0 or s-m < 0 or (s + m) % 2:
        print(-1)
    else:
        a = (s + m) // 2
        b = s - a
        print(max(a, b), min(a, b))
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------