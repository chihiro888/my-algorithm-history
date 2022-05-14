# 1 <= k <= 10000
# 1 <= n <= 1000000
# k <= n
k, n = map(int, input().split())
lanList = []
for _ in range(k):
    # 1 <= lan <= 2147483647
    lanList.append(int(input()))
    
# print(f'k = {k}, n = {n}')
# print(f'lanList = {lanList}')

minLan = min(lanList)

# print(f'minLan = {minLan}')

for L in range(minLan, 0, -1):
    # print(f'L = {L}')
    sumCutL = 0
    for lan in lanList:
        cutL = lan // L
        sumCutL += cutL
    # print(f'sumCutL = {sumCutL}')
    if sumCutL >= n:
        # print(f'L = {L}')
        print(L)
        break