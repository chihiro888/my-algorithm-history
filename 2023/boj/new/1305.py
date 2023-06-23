L = int(input())  # 전광판의 크기
ad_str = input()  # 현재 광고판에 보이는 문자열

N = len(ad_str)  # 광고문자열의 길이

# 전광판의 크기 L과 광고문자열의 길이 N을 비교하여 주기의 길이를 구함
period = 1
while period <= N:
    if ad_str[:period] == ad_str[period:2*period]:
        break
    period += 1

print(period)