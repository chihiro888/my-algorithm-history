import sys

# 1 <= N <= 10,000,000
n = int(input())
nList = [0] * 10001
for i in range(n):
    # 1 <= input <= 10,000
    nList[int(sys.stdin.readline())] += 1
for i in range(10001):
    if nList[i] != 0:
        for j in range(nList[i]):
            print(i)