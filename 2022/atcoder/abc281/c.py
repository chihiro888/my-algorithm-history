# 문제 입력
n, t = map(int, input().split())
a = list(map(int, input().split()))

# 연주 길이의 합
sa = sum(a)

# t 분을 연주 길이의 합으로 나누면 연산이 줄어듬
rest = t % sa

prev_s = 0  # 연주된 후 시점 (이전 값) 
s = 0       # 연주된 후 시점

idx = 0
while True:
    # 리스트 싸이클링
    if idx == n:
        idx = 0
        
    prev_s = s
 
    s += a[idx]
 
    # 연주된 후 시점이 목표를 넘어선 순간
    if s > rest:
        print(f'{idx+1}', end=' ')      # 곡의 번호는 인덱스 1부터 시작
        print(rest - prev_s, end=' ')   # 목표에서 연주된 후 시점을 빼면 시간이 나옴
        break
 
    idx += 1

    