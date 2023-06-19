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

# 문자열을 리스트로 변환
def str_to_list(s:str):
    return [x for x in s]

# 리스트를 문자열로 출력
def print_list(l: list):
    print(' '.join(map(str, l)))

# 리스트 안에 문자 치환
def replace_string_in_list(lst, target, replacement):
    for i in range(len(lst)):
        if lst[i] == target:
            lst[i] = replacement
    return lst