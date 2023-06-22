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
    a = int(ip()) # 현재 고기 온도
    b = int(ip()) # 목표 고기 온도
    c = int(ip()) # 얼음, 1도 데우는데 걸리는 시간
    d = int(ip()) # 고기를 해동하는데 걸리는 시간
    e = int(ip()) # 얼지않음, 1도 데우는데 걸리는 시간

    count = 0

    lock = False
    while not (a == b):
        if a < 0:
            # 얼은 고기
            a += 1
            count += c
        elif a == 0 and not lock:
            # 해동필요
            count += d
            lock = True
        elif a >= 0:
            # 얼지않은 고기
            a += 1
            count += e

    print(count)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------