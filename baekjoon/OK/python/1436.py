sixList = []
for n in range(0, 2710000):
    if str(n).find('666') != -1:
        sixList.append(n)

n = int(input())
print(sixList[n-1])