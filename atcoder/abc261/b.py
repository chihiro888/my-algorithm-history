
n = int(input())

data = []
for _ in range(0, n):
    x = [char for char in input()]
    data.append(x)

# print(f'data = {data}')

for i in range(0, n):
    for j in range(0, n):
        if i != j:
            if data[i][j] == 'W' and data[j][i] == 'W':
                print('incorrect')
                exit()
            elif data[i][j] == 'L' and data[j][i] == 'L':
                print('incorrect')
                exit()
            elif data[i][j] == 'W' and data[j][i] == 'D':
                print('incorrect')
                exit()
            elif data[i][j] == 'D' and data[j][i] == 'W':
                print('incorrect')
                exit()
            elif data[i][j] == 'L' and data[j][i] == 'D':
                print('incorrect')
                exit()
            elif data[i][j] == 'D' and data[j][i] == 'L':
                print('incorrect')
                exit()
print('correct')