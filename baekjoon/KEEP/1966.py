'''
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1

t
n m
a1 a2 ... an

t = 테스트케이스
n = 문서의 개수
m = queue에서 몇번 째
a = 중요도

example
A B C D
2 1 4 3

C D A B

1 2 '3' 4
2 '3' 4 1
'3' 4 1 2
1 2 '3'
2 '3' 1
'3' 1 2

'1' 1 9 1 1 1
1 9 1 1 1 '1'
9 1 1 1 '1' 1
'''

t = int(input())
for _ in range(t):
    # 1 <= n <= 100
    # 0 <= m <= n
    n, m = map(int, input().split())
    # 1 <= a <= 9
    a = list(map(int, input().split()))
    # a[m] = a[m]
    target = a[m]
    cnt = 0
    while(True):
        printTarget = a[0]
        maxA = max(a)
        print('a -> ', a)
        print('printTarget -> ', printTarget)
        if maxA == printTarget:
            a.pop(0)
            cnt += 1
            if maxA == target:
                break
        else:
            x = a.pop(0)
            a.append(x)

    print('cnt -> ', cnt)