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
    n = int(ip())
    s = ip()

    r = []
    for i in range(1, len(s)):
        l = 0
        for j in range(0, len(s)):

            if j+i > len(s)-1:
                break

            if s[j] != s[j+i]:
                l += 1
            else:
                break

        r.append(l)
    
    for d in r:
        print(d)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------