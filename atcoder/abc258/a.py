K = int(input())
S = 1260
solve = S + K
print(f'{solve // 60}:{str(solve % 60).zfill(2)}')