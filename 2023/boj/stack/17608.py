import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def solution(d):
    d.reverse()
    count = 0
    m = 0
    for x in d:
        if m < x:
            m = max(x, m)
            count += 1
    return count
# -------------------------------


# Please write the code below ---
def main():
    size = int(ip())
    d = []
    for _ in range(size):
        d.append(int(ip()))

    print(solution(d))
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------