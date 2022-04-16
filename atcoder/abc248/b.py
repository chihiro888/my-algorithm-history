'''
a - 슬라임 초기 개수
b - 슬라임 목표 개수
k - 슬라임 증식배율
'''

# 입력
a, b, k = map(int, input().split())

# 회차수
cnt = 0

# 슬라임 증식 후 개수
sum = a

# 처리
while(True):
    # 회차수 증가
    cnt += 1
    
    if a == b:
        # 슬라임 초기 개수와 슬라임 목표 개수가 동일할 경우
        print(0)
        break
    else:
        # 슬라임 초기 개수와 슬라임 목표 개수가 동일하지 않을 경우, 슬라임 증식
        sum = (sum * k)

    if b <= sum:
        # 증식 후 슬라임 목표 개수 이상일 경우
        print(cnt)
        break