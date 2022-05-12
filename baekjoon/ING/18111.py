n, m, b = map(int, input().split())
x = []
for _ in range(n):
    x += list(map(int, input().split()))
    
print(f'n = {n}, m = {m}, b = {b}')
print(f'x = {x}')

minX = min(x)
maxX = max(x)

print(f'minX = {minX}, maxX = {maxX}')

minT = 9999999999999999999
minFloor = 0
for floor in range(minX, maxX+1):
    t = 0
    block = b
    if floor == minX:
        for d in x:
            # remove block
            t += (d - minX) * 2
    else:
        for d in x:
            if d > floor:
                # remove block
                t += (d - floor) * 2
            elif d < floor:
                # add block
                addBlock = floor - d
                # print(f'addBlock = {addBlock}')
                if (block - addBlock) >= 0:
                    t += floor - d
                    block -= addBlock
                    print(f'block = {block}')
                else:
                    print('enough block')
                    t = 9999999999999999999
    
    if minT > t:
        minT = t
        minFloor = floor

    print(f'floor = {floor}, t = {t}')
    print('---------------')
    
print(f'{minT} {minFloor}')