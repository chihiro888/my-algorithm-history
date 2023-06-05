import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def solution(d):
    d = [x for x in d]
    lock = False
    result = []
    stack = []
    for e in d:
        if e == '<' and len(stack) == 0:
            lock = True
            result.append(e)
        elif e == '>':
            lock = False
            result.append(e)
        elif e == ' ':
            while len(stack) != 0:
                result.append(stack.pop())
            result.append(' ')
        elif e == '<' and len(stack) != 0:
            while len(stack) != 0:
                result.append(stack.pop())
            result.append('<')
            lock = True
        elif lock:
            result.append(e)
        elif not lock:
            stack.append(e)
    while len(stack) != 0:
        result.append(stack.pop())
    
    return ''.join(result)
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