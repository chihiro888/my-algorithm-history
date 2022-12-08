# 1 <= t <= 10000
t = int(input())
for _ in range(t):
    # 1 <= x, y <= 100
    x, y = map(int, input().split())
    
    if x > y:
        print(f'0 0')
    elif x == y:
        print(f'3 1')
    elif x < y:
        # a = times
        # b = * operator
        solveA = 0
        solveB = 0
        for a in range(1, 100):
            for b in range(2, 100):
                if x * (b ** a) == y:
                    solveA = a
                    solveB = b
                if x * (b ** a) > y:
                    break
        print(f'{solveA} {solveB}')