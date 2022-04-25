xList = []
yList = []
solve = []
for n in range(0, 3):
    d = list(map(int, input().split()))
    x = d[0]
    y = d[1]
    xList.append(x)
    yList.append(y)

if xList[0] == xList[1]:
    solve.append(xList[2])
elif xList[0] == xList[2]:
    solve.append(xList[1])
elif xList[1] == xList[2]:
    solve.append(xList[0])

if yList[0] == yList[1]:
    solve.append(yList[2])
elif yList[0] == yList[2]:
    solve.append(yList[1])
elif yList[1] == yList[2]:
    solve.append(yList[0])

print(f'{solve[0]} {solve[1]}')

'''
https://atcoder.jp/contests/abc246/submissions/30687236
'''