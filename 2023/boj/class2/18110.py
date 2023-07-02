import sys
from collections import deque


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def my_round(val):
    return int(val) + 1 if val - int(val) >= 0.5 else int(val)

def calculate_average(lst):
    if len(lst) == 0:
        return 0  # 리스트가 비어있을 경우 0을 반환하거나 원하는 처리를 수행할 수 있습니다.
    else:
        return my_round(sum(lst) / len(lst))
# -------------------------------


# Please write the code below ---
def main():
    size = int(ip())
    d = deque()
    for _ in range(size):
        d.append(int(ip()))
        
    d = deque(sorted(d))
    
    x = my_round(size * 0.15)
    
    for i in range(x):    
        d.pop()
        d.popleft()
    
    if size == 0:
        print(0)
    else:
        print(calculate_average(d))
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------