from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    d = deque(list(map(int, input().split())))
    
    idx = m
    cnt = 0
    try:
        while True:
            if len(d) == 0:
                print(1)
                break
            i = 0
            if max(d) != d[i]:
                x = d.popleft()
                d.append(x)
                if idx == 0:
                    idx = len(d) - 1
                else:
                    idx -= 1
            elif max(d) == d[i]:
                d.popleft()
                if idx == 0:
                    print(cnt + 1)
                    break
                else:
                    idx -= 1
                cnt += 1
    except BaseException:
        pass