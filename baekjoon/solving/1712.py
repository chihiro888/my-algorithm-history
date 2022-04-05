A, B, C = map(int, input().split())

'''
for n in range(0, 9999999999):
    if B > C:
        print(-1)
        break
    elif (A + (B * n)) < (C * n):
        print(n)
        break
'''

if B >= C:
    print(-1)
else:
    print(int(A / (C - B)) + 1)