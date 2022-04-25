import datetime
 
input = list(map(int, input().split()))
a = datetime.time(input[0], input[1], 0)
b = datetime.time(input[2], input[3], 1)

if (a < b):
    print('Takahashi')
else:
    print('Aoki')
    
'''
https://atcoder.jp/contests/abc245/submissions/30443122
'''