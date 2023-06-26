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
    tree = {}

    for _ in range(size):
        root, left, right = mv(str)
        tree[root] = [left, right]

    def preorder(root):
        if root != '.':
            print(root, end='')  # root
            preorder(tree[root][0])  # left
            preorder(tree[root][1])  # right
    
    
    def inorder(root):
        if root != '.':
            inorder(tree[root][0])  # left
            print(root, end='')  # root
            inorder(tree[root][1])  # right
    
    
    def postorder(root):
        if root != '.':
            postorder(tree[root][0])  # left
            postorder(tree[root][1])  # right
            print(root, end='')  # root

    preorder('A')
    print()
    inorder('A')
    print()
    postorder('A')

# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------