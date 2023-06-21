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
    while True:
        a, b, c = mv(str)
        
        if a == '#':
            break

        if int(b) > 17 or int(c) >= 80:
            print(f'{a} Senior')
        else:
            print(f'{a} Junior')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------