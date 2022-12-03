s = input()
t = input()

sl = [x for x in s]
tl = [x for x in t]

# print(f'sl = {sl}')
# print(f'tl = {tl}')

idx = 0
while True:
    try:
        if sl[idx] != tl[idx]:
            print(idx + 1)
            break
        idx += 1
    except BaseException:
        print(idx + 1)
        break