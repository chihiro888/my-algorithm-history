inputList = []
for n in range(0, 9):
    inputList.append(int(input()))

print(max(inputList))

idx = 1
for input in inputList:
    if input == max(inputList):
        print(idx)
    idx += 1