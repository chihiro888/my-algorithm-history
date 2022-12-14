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
