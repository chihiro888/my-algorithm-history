t = int(input())

print(f't = {t}')

for _ in range(t):
    # n 은 퀘스트
    # c 는 coin (코인)
    # d 는 day (일)
    # k 는 휴식
    n, c, d = map(int, input().split())
    print(f'n = {n}, c = {c}, d = {d}')

    # a 는 코인
    a = list(map(int, input().split()))
    print(f'a = {a}')

'''
4일동안 적어도 5코인

day = 1
1 coin

day = 2
2 coin

day = 3
1 coin

day = 4
2 coin
'''