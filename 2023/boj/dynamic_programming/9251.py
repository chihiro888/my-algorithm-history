import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
# 이차원 배열 디버깅
def print_arr(arr):
    for y in arr:
        for x in y:
            print(x, end='')
        print()
    print('----------------')


def longest_common_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)

    # 2차원 테이블을 생성하여 부분 수열의 길이를 저장
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 최장 공통 부분 수열 계산
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print_arr(dp)

    # 최장 공통 부분 수열의 길이 반환
    return dp[m][n]
# -------------------------------


# Please write the code below ---
def main():
    x = ip()
    y = ip()

    result = longest_common_subsequence(x, y)
    print(result)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------