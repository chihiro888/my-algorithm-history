import sys

T = int(sys.stdin.readline())

for n in range(1, T+1):
    I = list(map(int, sys.stdin.readline().split()))
    print(f'Case #{n}: {I[0]} + {I[1]} = {I[0] + I[1]}')