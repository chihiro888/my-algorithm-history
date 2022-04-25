i = input()

store = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

totalCnt = 0
for n in store:
    cnt = i.count(n)
    totalCnt += cnt
    i = i.replace(n, '9')
    
totalCnt += len(i.replace('9', ''))

print(totalCnt)