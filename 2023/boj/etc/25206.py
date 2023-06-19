import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def get_score(grade):
    if grade == 'A+':
        return 4.5
    elif grade == 'A0':
        return 4.0
    elif grade == 'B+':
        return 3.5
    elif grade == 'B0':
        return 3.0
    elif grade == 'C+':
        return 2.5
    elif grade == 'C0':
        return 2.0
    elif grade == 'D+':
        return 1.5
    elif grade == 'D0':
        return 1.0
    elif grade == 'F':
        return 0.0
# -------------------------------


# Please write the code below ---
def main():
    # 학점의 총합
    t1 = 0

    # 전공과목별의 합
    t2 = 0

    while True:
        d = ip()
        if d == "":
            break

        # input
        a, b, c = d.split(' ')
        b = float(b)

        # P 인 경우 처리 하지 않음
        if c == 'P':
            continue

        s = get_score(c)
        t = b * s
        t2 += t
        t1 += b

    print(round(t2/t1, 6))
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------