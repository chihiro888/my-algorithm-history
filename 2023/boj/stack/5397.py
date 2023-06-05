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

def solution(d):
    d = str_to_list(d)
    temp_stack = []
    current_stack = []
    for e in d:
        if e == '<' and len(current_stack) != 0:
            temp_stack.append(current_stack.pop())
        elif e == '>' and len(temp_stack) != 0:
            current_stack.append(temp_stack.pop())
        elif e == '-' and len(current_stack) != 0:
            current_stack.pop()
        elif e not in ['<', '>', '-']:
            current_stack.append(e)

    while len(temp_stack) != 0:
        current_stack.append(temp_stack.pop())
        
    print(''.join(current_stack))
# -------------------------------


# Please write the code below ---
def main():
    size = int(ip())
    for _ in range(size):
        d = ip()
        solution(d)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------