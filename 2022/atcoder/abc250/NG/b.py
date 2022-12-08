# 1 <= n, a, b <= 10
n, a, b = map(int, input().split())

am = n * a
an = n * b

if n == 1:
    for y in range(a):
        for x in range(b):
            print('.', end='')
        print()
else:
    white = True
    black = False
    for dm in range(1, am+1):
        for dn in range(1, an+1):
            if white:
                print('.', end='')
                if dn % b == 0:
                    white = False
                    black = True
            elif black:
                print('#', end='')
                if dn % b == 0:
                    white = True
                    black = False
        print()
        print(f'dm % a == 0 = {dm % a == 0}')
        if dm % a == 0 and a == 1:
            white, black = black, white