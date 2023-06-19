import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
# 정수를 입력받아 약수를 리스트로 반환
def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors
# -------------------------------


# Please write the code below ---
def main():
    while True:
        a, b = mv(int)

        if a == 0 and b == 0:
            break

        x = find_divisors(b)

        condition_a = a in x
        condition_b = a%b == 0

        if condition_a:
            print('factor')
        elif condition_b:
            print('multiple')
        else:
            print('neither')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------