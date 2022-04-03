import sys

while(True):
    I = list(map(int, sys.stdin.readline().split()))
    if I == []:
        break
    A = I[0]
    B = I[1]
    print(f'{A + B}')