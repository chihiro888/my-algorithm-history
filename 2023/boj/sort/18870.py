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
    # 입력
    size = int(ip())
    d = lmv(int)

    # 압축 사전 생성
    x = sorted(set(d))
    t = {}
    for i in range(0, len(x)):
        t[x[i]] = i

    # 압축
    for e in d:
        print(t[e], end=' ')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------