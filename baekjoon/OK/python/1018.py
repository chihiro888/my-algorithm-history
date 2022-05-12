def getDataList(m, n, c):
    dataList = []
    for y in range(0, m-7):
        for x in range(0, n-7):
            iCnt = 0
            data = ''
            for i in range(y, len(c)):
                jCnt = 0
                for j in range(x, len(c[0])):
                    data += c[i][j]
                    if jCnt == 7:
                        break
                    jCnt += 1
                if iCnt == 7:
                    break
                iCnt += 1
            dataList.append(data)
    return dataList

def solve(dataList):
    min = 9999
    priorityW = 'WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW'
    priorityB = 'BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB'
    for data in dataList:
        w = [ord(a) ^ ord(b) for a,b in zip(data, priorityW)]
        b = [ord(a) ^ ord(b) for a,b in zip(data, priorityB)]
        if w.count(21) < min:
            min = w.count(21)
        if b.count(21) < min:
            min = b.count(21)
    print(min)

def main():
    # init
    c = []

    # input
    m, n = map(int, input().split())
    for _ in range(m): c.append([ch for ch in input()])

    # solve
    dataList = getDataList(m, n, c)
    solve(dataList)

if __name__ == '__main__':
    main()