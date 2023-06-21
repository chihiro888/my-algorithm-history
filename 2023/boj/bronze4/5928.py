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
    # 11 / 11 / 11
    d, h, m = mv(int)
    
    x1 = 11 * 24 * 60 
    y1 = 11 * 60
    z1 = 11
    
    x2 = (d) * 24 * 60
    y2 = (h) * 60
    z2 = (m)
    
    t1 = x1 + y1 + z1
    t2 = x2 + y2 + z2
    
    if t2 - t1 >= 0:
        print(t2 - t1)
    else:
        print(-1)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------