import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def str_to_list(s:str):
    return [x for x in s]

def solution(d):
    d = str_to_list(d)
    stack = []
    for e in d:
        # 기본 처리
        if len(stack) != 0 and stack[-1] == '(' and e == ')':
            stack.pop()
            stack.append(2)
        elif len(stack) != 0 and stack[-1] == '[' and e == ']':
            stack.pop()
            stack.append(3)
        else:
            stack.append(e)

        # 후처리
        if len(stack) > 2 and stack[-3] == '[' and stack[-1] == ']':
            x = stack[-2] * 3
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append(x)

        if len(stack) > 2 and stack[-3] == '(' and stack[-1] == ')':
            x = stack[-2] * 2
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append(x)

        if len(stack) > 1 and isinstance(stack[-2], int) and isinstance(stack[-1], int):
            x = stack[-2] + stack[-1]
            stack.pop()
            stack.pop()
            stack.append(x)

    # 결과 반환
    if len(stack) == 1:
        return stack[0]
    else:
        return 0
# -------------------------------


# Please write the code below ---
def main():
    d = ip()
    result = solution(d)
    print(result)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------