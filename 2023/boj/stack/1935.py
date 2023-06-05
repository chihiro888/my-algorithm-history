import sys
import string


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def str_to_list(s:str):
    return [x for x in s]

def replace_string_in_list(lst, target, replacement):
    for i in range(len(lst)):
        if lst[i] == target:
            lst[i] = replacement
    return lst

def double_pop(stack):
    stack.pop()
    stack.pop()

def stack_cal(d):
    stack = []
    for e in d:
        if e == '*':
            r = stack[-2] * stack[-1]
            double_pop(stack)
            stack.append(r)
        elif e == '+':
            r = stack[-2] + stack[-1]
            double_pop(stack)
            stack.append(r)
        elif e == '-':
            r = stack[-2] - stack[-1]
            double_pop(stack)
            stack.append(r)
        elif e == '/':
            r = stack[-2] / stack[-1]
            double_pop(stack)
            stack.append(r)
        else:
            stack.append(e)

    return  f"{stack[0]:.2f}"
# -------------------------------


# Please write the code below ---
def main():
    # 문제입력 및 전처리
    size = int(ip())
    d = ip()
    d = str_to_list(d)
    alphabet = list(string.ascii_uppercase)
    for idx in range(size):
        d = replace_string_in_list(d, alphabet[idx], int(ip()))
    result = stack_cal(d)
    print(result)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------