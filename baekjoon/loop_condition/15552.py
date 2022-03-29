import sys

T = int(sys.stdin.readline())

for n in range(0, T):
    I = list(map(int, sys.stdin.readline().split()))
    print(I[0] + I[1])