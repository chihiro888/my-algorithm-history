# input
t = int(input())
for _ in range(t):
    # 2 <= s <= 50
    s = input()

    # init
    charList = [char for char in s]
    stack = []
    balance = True

    # check balance
    for char in charList:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                balance = False
                break
            else:
                x = stack.pop()

    # check rest item
    if len(stack) > 0:
        balance = False
                
    # solve
    if balance:
        print('YES')
    else:
        print('NO')