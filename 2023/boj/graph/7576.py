import sys
from collections import deque


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def bfs(g, q, m, n):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 0:
                g[nx][ny] = g[x][y] + 1
                q.append([nx, ny])

    return g
# -------------------------------


# Please write the code below ---
def main():
    # 입력
    m, n = mv(int)
    g = []
    for _ in range(n):
        g.append(lmv(int))

    # 초기 큐 세팅
    q = deque([])
    for i in range(n):
        for j in range(m):
            if g[i][j] == 1:
                q.append([i, j])

    # BFS 처리
    bfs(g, q, m, n)

    # 정답 추출
    sol = 0
    for i in g:
        for j in i:
            if j == 0:
                print(-1)
                exit(0)
        sol = max(sol, max(i))
    print(sol - 1)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------