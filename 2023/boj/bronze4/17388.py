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
    s, k, h = mv(int)
    c = s + k + h < 100
    if s + k + h >= 100:
        print('OK')
    elif c:
        x = [s, k, h]
        i = x.index(min(x)) 
        if i == 0:
            print('Soongsil')
        elif i == 1:
            print('Korea')
        elif i == 2:
            print('Hanyang')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------