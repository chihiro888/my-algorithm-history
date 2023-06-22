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
    a = int(ip())
    e = int(ip())

    if a >= 3 and e <= 4:
        print('TroyMartian')

    if a <= 6 and e >= 2:
        print('VladSaturnian')

    if a <= 2 and e <= 3:
        print('GraemeMercurian')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------