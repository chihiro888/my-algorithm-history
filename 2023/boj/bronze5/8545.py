import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def str_to_list(s:str):
    return [x for x in s]

def print_list(l: list):
    for x in l:
        print(x, end='')
# -------------------------------


# Please write the code below ---
def main():
    x = ip()
    x = str_to_list(x)
    x.sort(reverse=True)
    print_list(x)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------