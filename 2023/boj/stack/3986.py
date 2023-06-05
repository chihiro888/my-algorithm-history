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

def checkGoodWord(d):
    d = str_to_list(d)
    stack = []

    for e in d:
        if len(stack) > 1 and stack[-1] == e:
            stack.pop()
        else:
            stack.append(e)

    if len(stack) == 2 and stack[-1] == stack[-2]:
        return True
    else:
        return False
# -------------------------------


# Please write the code below ---
def main():
    size = int(ip())
    count = 0
    for _ in range(size):
        if checkGoodWord(ip()):
            count += 1
    print(count)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------