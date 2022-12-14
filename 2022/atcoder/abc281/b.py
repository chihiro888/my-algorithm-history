s = input()
sl = [x for x in s]

if len(s) == 8:
    if sl[0].isdigit() or sl[-1].isdigit():
        print('No')
    else:
        try:
            x = int(sl[1] + sl[2] + sl[3] + sl[4] + sl[5] + sl[6])
        except BaseException:
            print('No')
            exit()
        if 100000 <= x and x <= 999999:
            print('Yes')
        else:
            print('No')
else:
    print('No')