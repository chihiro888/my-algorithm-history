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
    d = [int(ip()) for _ in range(4)]
    
    if d[0] == d[1] and d[1] == d[2] and d[2] == d[3]:
        print('Fish At Constant Depth')
    elif is_sorted(d):
        print('Fish Rising')
    elif is_reverse_sorted(d):
        print('Fish Diving')
    else:
        print('No Fish.')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------