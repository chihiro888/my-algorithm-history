import sys


# Utilities ---------------------
debug = False
def p(name, value):
    if debug: print(f'{name} = {value}')
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
# -------------------------------


# Function Block ----------------

# -------------------------------


# Please write the code below ---
def main():
    t = int(ip())
    cute = 0
    not_cute = 0
    for _ in range(0, t):
        if int(ip()) == 1:
            cute += 1
        else:
            not_cute += 1
    if cute > not_cute:
        print('Junhee is cute!')
    else:
        print('Junhee is not cute!')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------