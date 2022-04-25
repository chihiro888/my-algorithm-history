N = input()
num = N
cnt = 0

while True:
    if len(num) == 1:
        num = '0' + num
    sum = str(int(num[0]) + int(num[1]))
    num = num[-1] + sum[-1]
    cnt += 1
    if int(num) == int(N):
        print(cnt)
        break
    