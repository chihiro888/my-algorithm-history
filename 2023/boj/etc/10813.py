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
    d = lmv(int)
    s = [i for i in range(1, d[0]+1)]
    for _ in range(d[1]):
        x = lmv(int)
        t = s[x[0]-1]
        s[x[0]-1] = s[x[1]-1]
        s[x[1]-1] = t
        
    print(' '.join(map(str, s)))
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------