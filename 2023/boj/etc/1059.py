import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------

# -------------------------------


# Please write the code below ---
def main():
    size = int(ip())
    s = lmv(int)
    t = int(ip())
    s.sort()

    for idx in range(size-1):
        if s[idx] < t and t < s[idx+1]:
            break
    
    start = s[idx]
    end = s[idx+1]

    print(f'start = {start}')
    print(f'end = {end}')
    print(f't = {t}')

    count = 0
    for i in range(start+1, end):
        for j in range(start+1, end):
            if i != j and i <= j and i <= t and i <= j:
                print([i, j])
                count += 1

    print(count)


# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------