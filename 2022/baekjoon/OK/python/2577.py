def split(word):
    return [char for char in word]
    
inputList = []
for n in range(0, 3):
    inputList.append(int(input()))

result = inputList[0] * inputList[1] * inputList[2]
resultList = split(str(result))

for n in range(0, 10):
    print(resultList.count(str(n)))