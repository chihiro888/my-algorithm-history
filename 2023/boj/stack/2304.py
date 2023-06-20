import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def solution(d):
    stack = []
    print(d)

    for e in d:
        if len(stack) > 1 and stack[-2][1] > stack[-1][1] and stack[-1][1] < e[1]:
            stack.pop()
            stack.append(e)
        else:
            stack.append(e)
        
    dd = stack
    for e in dd:
        if len(stack) > 1 and stack[-2][1] > stack[-1][1] and stack[-1][1] < e[1]:
            stack.pop()
            stack.append(e)
        else:
            stack.append(e)
        
    new_data = {}
    for e in stack:
        new_data[e[0]] = e[1]
    
    print(new_data)
    
    start = stack[0][0]
    end = stack[-1][0]
    print(f'start = {start}, end = {end}')
    for idx in range(start, end+1):
        if idx not in new_data:
            k = 1
            while True:
                try:
                    new_data[idx] = min(new_data[idx-1], new_data[idx+k])
                    break
                except BaseException:
                    k += 1
    
    print(new_data)
    value_list = list(new_data.values())
    print(value_list)
    
    
    return sum(value_list)
# -------------------------------


# Please write the code below ---
def main():
    # 입력 및 전처리
    size = int(ip())
    d = []
    for _ in range(size):
        d.append(lmv(int))
    d = sorted(d, key=lambda x: x[0])
    
    # 문제풀이
    print(solution(d))
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------