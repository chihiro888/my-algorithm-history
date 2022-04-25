N = int(input())

inputList = []
for n in range(0, N):
    inputList.append(input())

solve = inputList[0]

for idx in range(0, len(inputList[0])):
    backup = None
    unMatch = False
    for data in inputList:
        if (backup != None) and (backup != data[idx]):
            unMatch = True
        backup = data[idx]
    if unMatch:
        solve = solve[:idx] + '?' + solve[idx+1:]

print(solve)