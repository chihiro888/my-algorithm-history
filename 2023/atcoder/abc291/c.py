import sys
import re


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
# -------------------------------


# Please write the code below ---
def main():
    n = int(ip())
    s = ip()

    visited = set()  # 이미 방문한 좌표를 저장할 set
    visited.add((0, 0))

    x, y = 0, 0  # 현재 위치를 저장할 변수

    for move in s:
        if move == 'R':
            x += 1
        elif move == 'L':
            x -= 1
        elif move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        
        # print(f'({x}, {y})')

        # 현재 위치가 이미 방문한 좌표인 경우 Yes를 출력하고 프로그램 종료
        if (x, y) in visited:
            print("Yes")
            exit()
        else:
            visited.add((x, y))
            
    # 모든 이동을 마쳤지만 이미 방문한 좌표가 없는 경우 No를 출력
    print("No")

# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------