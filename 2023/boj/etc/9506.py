import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    # 자기 자신 생략
    divisors.pop()
    if n == sum(divisors):
        print(f"{n} =", ' + '.join(map(str, divisors)))
    else:
        print(f"{n} is NOT perfect.")
# -------------------------------


# Please write the code below ---
def main():
    while True:
        d = int(ip())
        if d == -1:
            break
        f = find_divisors(d)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------