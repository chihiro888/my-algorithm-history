import sys
from collections import deque

# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def josephus_permutation(N, K):
    # 초기 숫자 리스트 생성
    numbers = list(range(1, N + 1))
    
    # 결과를 저장할 리스트 생성
    result = []
    
    # 큐 생성
    queue = deque(numbers)
    
    while queue:
        # K번째 숫자를 제거하고 결과 리스트에 추가
        for _ in range(K - 1):
            queue.append(queue.popleft())
        result.append(queue.popleft())
    
    return result
# -------------------------------


# Please write the code below ---
n, k = mv(int)
permutation = josephus_permutation(n, k)
print("<" + ", ".join(map(str, permutation)) + ">")
# -------------------------------