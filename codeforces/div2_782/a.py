t = int(input())
for _ in range(t):
    n, r, b = map(int, input().split())
    max_r_cnt = 0
    for _ in range(n):
        if r > 0 and max_r_cnt < 3:
            print('R', end='')
            r -= 1
            max_r_cnt += 1
        elif b > 0:
            print('B', end='')
            b -= 1
            max_r_cnt = 0
    print() 