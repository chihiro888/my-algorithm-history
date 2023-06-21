import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
# 자리수 출력 제한
def format_float(n: float):
    return "{:.2f}".format(n)
# -------------------------------


# Please write the code below ---
def main():
    while True:
        n = float(ip())

        if n == -1:
            break

        print(f'Objects weighing {format_float(n)} on Earth will weigh {format_float(n * 0.167)} on the moon.')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------