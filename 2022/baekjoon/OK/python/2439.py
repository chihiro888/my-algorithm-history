import sys

T = int(sys.stdin.readline())

S = T-1
for n in range(1, T+1):
    print(f'{" " * S}{"*" * n}')
    S -= 1