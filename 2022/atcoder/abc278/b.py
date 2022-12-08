def isTime(h:str, m:str):
    if (0 <= int(h) <= 23) and 0 <= int(m) <= 59:
        return True
    else:
        return False

def main():
    h, m = map(str, input().split())

    if len(h) == 1:
        h = '0' + h

    if len(m) == 1:
        m = '0' + m

    nh = h[0] + m[0]
    nm = h[1] + m[1]

    # print(f'old = {h} {m}, new = {nh} {nm}')

    if isTime(nh, nm):
        print(f'{h} {m}')
    else:
        print(f'{(int(h)+1)%24} 0')

if __name__ == "__main__":
    main()