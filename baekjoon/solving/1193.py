X = int(input())

# init
row = 1
col = 1
up = False
down = False

for n in range(1, 10000000):
    # move
    if row == 1 and (not down):
        col += 1
        up = False
        down = True
    elif col == 1 and (not up):
        row += 1
        up = True
        down = False
    elif up:
        row -= 1
        col += 1
    elif down:
        row += 1
        col -= 1

    # print solution
    if X == 1:
        print('1/1')
        break
    elif X == n+1:
        print(f'{row}/{col}')
        break