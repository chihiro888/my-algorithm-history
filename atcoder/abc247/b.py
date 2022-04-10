# FAIL / AC x 14 / WA x 3

N = int(input())
 
# solve
condition = 'Yes'
 
# init
stList = []
sList = []
tList = []
for n in range(N):
    s, t = input().split()
    stList.append(f'{s} {t}')
    sList.append(s)
    tList.append(t)
 
if len(stList) != len(list(set(stList))):
    condition = 'No'
 
for s in sList:
    if s in tList:
        condition = 'No'
        
print(condition)