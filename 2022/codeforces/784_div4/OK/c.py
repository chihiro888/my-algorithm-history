# 1 <= t <= 100
from re import X
 
 
t = int(input())
 
 
for _ in range(t):
    # 2 <= n <= 50
    n = int(input())
    
    # 1 <= ai <= 1000
    a = list(map(int, input().split()))
    odd_i = []
    even_i = []
    for i in range(0, len(a)):
        if i % 2:
            even_i.append(a[i]+1)
        else :
            odd_i.append(a[i]+1)
    x1 = len([num for num in odd_i if num % 2 == 0])
    x2 = len([num for num in odd_i if num % 2 == 1])
    y1 = len([num for num in even_i if num % 2 == 0])
    y2 = len([num for num in even_i if num % 2 == 1])
    cnt_list = []
    cnt_list.append(x1)
    cnt_list.append(x2)
    cnt_list.append(y1)
    cnt_list.append(y2)
    if cnt_list.count(0) == 2:
        print('YES')
    else:
        print('NO')