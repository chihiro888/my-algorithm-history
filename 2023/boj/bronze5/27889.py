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
    if s == 'NLCS':
        print('North London Collegiate School')
    elif s == 'BHA':
        print('Branksome Hall Asia')
    elif s == 'KIS':
        print('Korea International School')
    elif s == 'SJA':
        print('St. Johnsbury Academy')

# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------