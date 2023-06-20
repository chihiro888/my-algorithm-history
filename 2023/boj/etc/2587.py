import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def calculate_average(lst):
    return int(sum(lst) / len(lst))

def calculate_median(lst):
    sorted_lst = sorted(lst)
    length = len(sorted_lst)
    
    if length % 2 == 1:
        return sorted_lst[length // 2]
    else:
        middle_right = length // 2
        middle_left = middle_right - 1
        return (sorted_lst[middle_left] + sorted_lst[middle_right]) / 2
# -------------------------------


# Please write the code below ---
def main():
    x = [int(ip()) for _ in range(5)]
    print(calculate_average(x))
    print(calculate_median(x))
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------