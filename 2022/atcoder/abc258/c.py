from collections import deque 

N, Q = map(int, input().split())
S = input()
charList = deque([char for char in S])
for _ in range(0, Q):
    o, c = map(int, input().split())
    if (o == 1):
        for _ in range(0, c):
            x = charList.pop()
            charList.appendleft(x)
    elif (o == 2):
        print(charList[c-1])