import sys


debug = False

def p(name, value):
    if debug: print(f'{name} = {value}')
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())


# '시간', '분', '초'를 입력받아 '초'로 변경함
def time_to_sec(h:int, m:int, s:int):
    xh = h * 60 * 60
    xm = m * 60
    xs = s
    return xh + xm + xs


# '초'를 입력받아 '시간', '분', '초'를 반환함
def sec_to_time(s:int):
    hh = s // 60 // 60
    s -= (hh * 60 * 60)
    mm = s // 60
    s -= (mm * 60)
    ss = s
    return hh, mm, ss


def main():
    h, m, s = mv(int)
    ts = int(ip())
    hh, mm, ss = sec_to_time(time_to_sec(h, m, s) + ts)
    print(f'{hh%24} {mm} {ss}')


if __name__ == "__main__":
    main()


