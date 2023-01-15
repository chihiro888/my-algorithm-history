import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def view(v):
    for x in v:
        print(x)
    print('-----------------------')
# -------------------------------


# Please write the code below ---
def main():
    n, m = mv(int)
    r, c, d = mv(int)
    v = []
    for _ in range(n):
        v.append(lmv(str))

    v[r][c] = '*'
    cnt = 1

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    while True:
        all = True
        for _ in range(4):
            nx = r + dx[(d+3)%4]
            ny = c + dy[(d+3)%4]

            d = (d + 3) % 4

            if 0 <= nx < n and 0 <= ny < m and v[nx][ny] == '0':
                v[nx][ny] = '*'
                cnt += 1

                r = nx
                c = ny

                all = False
                break

        if all:
            if v[r-dx[d]][c-dy[d]] == '1':
                print(cnt)
                break
            else:
                r, c = r-dx[d], c-dy[d]
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------