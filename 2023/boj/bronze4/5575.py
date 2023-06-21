import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
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

# -------------------------------


# Please write the code below ---
def main():
    for _ in range(3):
        sh, sm, ss, eh, em, es = mv(int)
        x = time_to_sec(sh, sm, ss)
        y = time_to_sec(eh, em, es)
        z = y - x
        kh, km, ks = sec_to_time(z)
        print(f'{kh} {km} {ks}')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------