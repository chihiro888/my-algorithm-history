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
        a, b, c = mv(int)

        if a == 0 and b == 0 and c == 0:
            break

        if a == b == c:
            print("Equilateral")
        elif 2 * max(a, b, c) >= a + b + c:
            print("Invalid")
        elif a == b or b == c or a == c:
            print("Isosceles")
        else:
            print("Scalene")


# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------