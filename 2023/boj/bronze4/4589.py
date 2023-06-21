import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
# 정렬 유무 확인
def is_sorted(seq):
    return all(seq[i] <= seq[i+1] for i in range(len(seq)-1))

# 역정렬 유무 확인
def is_reverse_sorted(seq):
    return all(seq[i] >= seq[i+1] for i in range(len(seq)-1))
# -------------------------------


# Please write the code below ---
def main():
    t = int(ip())
    print('Gnomes:')
    for _ in range(t):
        x = lmv(int)
        if is_sorted(x) or is_reverse_sorted(x):
            print('Ordered')
        else:
            print('Unordered')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------