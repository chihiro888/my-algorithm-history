n = int(input())
d = []
for _ in range(n):
    d.append(list(map(int, input().split())))
    
# print(f'n = {n}')
# print(f'd = {d}')

memo = [0 for _ in range(2**(n))]
memo[0] = d[0][0]

'''
# i = 0
memo[0] = d[0][0]

# i = 1
memo[1] = memo[0] + d[1][0]
memo[2] = memo[0] + d[1][1]

# i = 2
memo[3] = memo[1] + d[2][0]
memo[4] = memo[1] + d[2][1]
memo[5] = memo[2] + d[2][1]
memo[6] = memo[2] + d[2][2]

# i = 3
memo[7] = memo[3] + d[3][0]
memo[8] = memo[3] + d[3][1]
memo[9] = memo[4] + d[3][1]
memo[10] = memo[4] + d[3][2]
memo[11] = memo[5] + d[3][1]
memo[12] = memo[5] + d[3][2]
memo[13] = memo[6] + d[3][2]
memo[14] = memo[6] + d[3][3]

# i = 4
memo[15] = memo[7] + d[4][0]
memo[16] = memo[7] + d[4][1]
memo[17] = memo[8] + d[4][1]
memo[18] = memo[8] + d[4][2]
memo[19] = memo[9] + d[4][1]
memo[20] = memo[9] + d[4][2]
memo[21] = memo[10] + d[4][2]
memo[22] = memo[10] + d[4][3]
memo[23] = memo[11] + d[4][1]
memo[24] = memo[11] + d[4][2]
memo[25] = memo[12] + d[4][2]
memo[26] = memo[12] + d[4][3]
memo[27] = memo[13] + d[4][2]
memo[28] = memo[13] + d[4][3]
memo[29] = memo[14] + d[4][3]
memo[30] = memo[14] + d[4][4]
'''

p = [0]
q = []

for i in range(1, n):
    q.clear()
    for e in p:
        q.append(e + 1)
    p = p + q  
    # print(f'p = {p}')
    idx = 0
    for j in range((2**i)-1, ((2**i)-1)+((2**i))):
        memo[j] = memo[(j-1)//2] + d[i][p[idx]]
        # print(f'i = {i}, j = {j}, x = {(j-1)//2}, y = {p[idx]}')
        # print(f'memo = {memo}') 
        idx += 1
    # print('--------------')

# print(f'len(memo) = {len(memo)}')     
print(f'memo = {memo}') 
# print('-------------- solve')
print(max(memo))