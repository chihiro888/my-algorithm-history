import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
# 문자열을 리스트로 변환
def str_to_list(s:str):
    return [x for x in s]

# 리스트를 문자열로 반환
def get_str(l: list):
    return ''.join(map(str, l))

# 풀이
def solution(lst):
    for i in range(len(lst)):
        if lst[i] == 'i':
            lst[i] = 'e'
        elif lst[i] == 'e':
            lst[i] = 'i'
        elif lst[i] == 'I':
            lst[i] = 'E'
        elif lst[i] == 'E':
            lst[i] = 'I'
    return get_str(lst)
# -------------------------------


# Please write the code below ---
def main():
    while True:
        s = ip()
        s = str_to_list(s)
        
        if len(s) == 0:
            break
        s = solution(s)
        print(s)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------