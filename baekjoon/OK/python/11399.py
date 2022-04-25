# input
count = int(input())
dataList = list(map(int, input().split()))

# solve
def solve(count, dataList):
    result = []
    dataList.sort()
    for i in range(count):
        if(i == 0):
            result.append(dataList[i])
        else:
            result.append(dataList[i] + result[i-1])
    print(sum(result))

# result
solve(count, dataList)