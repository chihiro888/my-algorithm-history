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
    d = []
    for _ in range(3):
        d.append(int(ip()))
    
    
    if d.count(60) == 3:
        print('Equilateral')
    elif sum(d) != 180:
        print('Error')
    elif sum(d) == 180 and d[0] != d[1] and d[1] != d[2] and d[0] != d[2]:
        print('Scalene')
    else:
        print('Isosceles')

# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------