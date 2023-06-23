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
    c = []
    for _ in range(size):
        a, d, g = mv(int)
        y = d + g
        x = y * a

        if a == y:
            x = x * 2
        
        c.append(x)
    
    print(max(c))
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------