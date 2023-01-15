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
    # print(f'n = {n}')
    s_list = []
    t_list = []
    for _ in range(n):
        s, t = mv(str)
        # print(f's = {s}, t = {t}')
        s_list.append(s)
        t_list.append(t)

    s_list = sorted(list(set(s_list)))
    t_list = sorted(list(set(t_list)))

    # print(f's_list = {s_list}')
    # print(f't_list = {t_list}')

    if s_list != t_list:
        print('Yes') 
    else:
        print('No')
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------