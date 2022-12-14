import sys


# Utilities ---------------------
debug = False
def p(name, value):
    if debug: print(f'{name} = {value}')
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
# -------------------------------


# Function Block ----------------
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
# -------------------------------


# Please write the code below ---
def main():
    s = ip()
    print(1 if is_palindrome(s) else 0)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------