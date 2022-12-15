import sys
from collections import deque


# Utilities ---------------------
debug = True
def p(name, value):
    if debug: print(f'{name} = {value}')
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
# -------------------------------


# Function Block ----------------
# 에라토스테네스의 체
def prime_list(n):
    s = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if s[i] == True:
            for j in range(i+i, n, i):
                s[j] = False
    return [i for i in range(2, n) if s[i] == True]

# BFS 응용
def bfs(s, e, p):
    q = deque()
    q.append([s, 0])
    v = [0 for _ in range(10000)]
    v[s] = 1

    while q:
        cur, cnt = q.popleft()
        cur = str(cur)

        if int(cur) == e:
            return cnt

        for i in range(4):
            for j in range(10):
                t = int(cur[:i] + str(j) + cur[i+1:])
                
                # 1000 보다 크다, 방문 X, 소수 O
                if t >= 1000 and v[t] == 0 and p.count(t) != 0:
                    v[t] = 1
                    q.append([t, cnt + 1])
# -------------------------------


# Please write the code below ---
def main():
    t = int(ip())
    p = prime_list(10)
    for _ in range(t):
        s, e = mv(int)
        cnt = bfs(s, e, p)
        print(cnt if cnt != None else 0 )
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------