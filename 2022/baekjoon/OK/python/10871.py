import sys

I = list(map(int, sys.stdin.readline().split()))
N = I[0]
X = I[1]
A = list(map(int, sys.stdin.readline().split()))

for n in A:
    if n < X:
        print(n)