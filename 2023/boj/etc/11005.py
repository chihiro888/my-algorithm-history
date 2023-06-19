import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def base_convert(number, base):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    while number > 0:
        number, remainder = divmod(number, base)
        result = alphabet[remainder] + result
    
    return result
# -------------------------------


# Please write the code below ---
def main():
    a, b = mv(int)
    print(base_convert(a, b))
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------