d = list(map(int, input().split()))

asc = True
des = True
for n in range(1, 9):
    if d[n-1] != n:
        asc = False
        
d.reverse()
for n in range(1, 9):
    if d[n-1] != n:
        des = False
              
if asc:
    print("ascending")
elif des:
    print("descending")
elif not asc and not des:
    print("mixed")