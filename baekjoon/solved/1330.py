input = list(map(int, input().split()))

if input[0] > input[1]:
    print('>')
elif input[0] < input[1]:
    print('<')
else:
    print('==')