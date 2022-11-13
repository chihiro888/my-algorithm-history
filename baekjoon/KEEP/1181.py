import sys
from operator import itemgetter

def removeDuplicate(dataList):
    resultList = []
    for i in range(len(dataList)):
        if dataList[i] not in dataList[i + 1:]:
            resultList.append(dataList[i])
    return resultList
            
n = int(input())
data = []

# O(N)
for _ in range(n):
    word = sys.stdin.readline().strip()
    data.append({'word': word, 'length': len(word)})

# O(?)
data = sorted(data, key=itemgetter('length', 'word')) 

# O(N)
data = removeDuplicate(data)

# O(N)
for d in data:
    print(d['word'])