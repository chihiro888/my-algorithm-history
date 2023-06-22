import sys
from datetime import date

# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def calculate_age(birthdate, reference_date):
    age = reference_date.year - birthdate.year
    
    # birthdate의 월과 일을 이용하여 생일이 지났는지 체크
    if reference_date.month < birthdate.month or (reference_date.month == birthdate.month and reference_date.day < birthdate.day):
        age -= 1
    
    return age

# -------------------------------


# Please write the code below ---
def main():
    y, m, d = mv(int)
    by, bm, bd = mv(int)

    curr = date(y, m, d)
    base = date(by, bm, bd)
    x = calculate_age(curr, base)

    print(x)
    print(by-y+1)
    print(by-y)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------