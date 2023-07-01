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
    s = int(ip())
    p = int(ip())
    
    d = []
    if s < 5:
        d.append(p)
    if 5 <= s:
        d.append(int(p - 500))
    if 10 <= s:
        d.append(int(p - (p * 0.1)))
    if 15 <= s:
        d.append(int(p - 2000))
    if 20 <= s:
        d.append(int(p - (p * 0.25)))
    
    x = min(d)
    
    if x > 0:
        print(x)
    else:
        print(0)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------