import sys
from collections import deque


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
    n, k = mv(int)

    if n == k:
        print(0)
        exit(0)

    # 큐 초기세팅
    q = deque()
    q.append([n-1, n+1, n*2, 1])

    v = []    
    solve = 0
    while not len(q) == 0:
        d = q.popleft()

        if k in d[0:3]:
            solve = d[3]
            break

        for x in d[:len(d)-1]:
            if x not in v and x < 100001:
                v.append(x)
                q.append([x-1, x+1, x*2, d[3]+1])

    print(solve)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------