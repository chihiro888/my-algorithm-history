import statistics

C = int(input())

for n in range(0, C):
    aboveCnt = 0
    dataList = list(map(int, input().split()))
    dataList.pop(0)
    avg = statistics.mean(dataList)
    for data in dataList:
        if data > avg:
            aboveCnt += 1
    print(f'{round(aboveCnt/len(dataList) * 100, 3):.3f}%')