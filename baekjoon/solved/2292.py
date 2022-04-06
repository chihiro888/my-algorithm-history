N = int(input())

start = 2
layer = 1
while True:
    if N == 1:
        print(1)
        break
    start += layer * 6
    layer += 1
    if start > N:
        print(layer)
        break