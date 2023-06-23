import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def print_pattern(n):
    # 위쪽 삼각형 출력
    for i in range(n):
        # 왼쪽 공백 출력
        for j in range(i):
            print(" ", end="")

        # 별표 출력
        for j in range(2 * (n - i) - 1):
            print("*", end="")

        print()  # 줄 바꿈
# -------------------------------


# Please write the code below ---
def main():
    n = int(ip())
    print_pattern(n)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------