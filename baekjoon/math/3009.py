xList = []
yList = []
for _ in range(3):
    x, y = map(int, input().split())
    xList.append(x)
    yList.append(y)

if xList[0] == xList[1]:
    print(xList[2], end=' ')
elif xList[1] == xList[2]:
    print(xList[0], end=' ')
else:
    print(xList[1], end=' ')
    
if yList[0] == yList[1]:
    print(yList[2])
elif yList[1] == yList[2]:
    print(yList[0])
else:
    print(yList[1])
    
    