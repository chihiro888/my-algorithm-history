import sys

while(True):
    I = list(map(int, sys.stdin.readline().split()))
    A = I[0]
    B = I[1]
    if A == 0 and B == 0:
        break
    print(f'{A + B}')
    