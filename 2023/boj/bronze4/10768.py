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
    m = int(ip())
    d = int(ip())

    if m == 2 and d == 18:
        print('Special')
    elif m == 2 and d < 18:
        print('Before')
    elif m < 2:
        print('Before')
    elif m == 2 and d > 18:
        print('After')
    else:
        print('After')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------