import sys


# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------


# Function Block ----------------
def dfs(tree, size, target):
    tree[target] = -2
    for i in range(size):
        if target == tree[i]:
            dfs(tree, size, i)
# -------------------------------


# Please write the code below ---
def main():
    size = int(ip())
    tree = lmv(int)
    target = int(ip())
    
    print(tree)
    
    dfs(tree, size, target)
    
    print(tree)
    
    count = 0
    for i in range(size):
        if tree[i] != -2 and i not in tree:
            count += 1
            
    print(count)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------