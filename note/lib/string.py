# 팰린드롬 문자열 검증
def is_palindrome(s):
    result = True
    start = 0
    end = len(s)-1
    if len(s) % 2 == 0: loop = len(s) // 2
    else: loop = (len(s) // 2) + 1
    for _ in range(0, loop):
        if s[start] != s[end]:
            result = False
            break
        start += 1
        end -= 1
    return result