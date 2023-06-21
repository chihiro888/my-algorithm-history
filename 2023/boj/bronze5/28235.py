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
    if s == 'SONGDO':
        print('HIGHSCHOOL')
    elif s == 'CODE':
        print('MASTER')
    elif s == '2023':
        print('0611')
    elif s == 'ALGORITHM':
        print('CONTEST')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------