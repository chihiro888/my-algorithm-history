import sys


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
    # input
    x = []
    while True:
        d = ip()
        if d == '':
            break
        x.append(str_to_list(d))

    # solution
    for i in range(15):
        for j in range(15):
            try:
                print(x[j][i], end='')
            except BaseException:
                pass

# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------