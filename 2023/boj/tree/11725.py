import sys
sys.setrecursionlimit(10**6)

# Utilities ---------------------
def ip(): return sys.stdin.readline().strip()
def ips(): return sys.stdin.readline().strip().split()
def mv(type): return map(type, ips())
def lmv(type): return list(map(type, ips()))
# -------------------------------



# Function Block ----------------
def bfs(size, tree, node):
    # 큐 초기화
    queue = [node]

    # 부모 저장공간 초기화
    parent = [0] * (size+1)

    # 방문 저장곤간 초기화
    visited = [0] * (size+1)

    # 큐가 비워질 때 까지 반복
    while not len(queue) == 0:
        node = queue.pop(0)

        # 방문 처리
        visited[node] = 1 

        # BFS
        for _node in tree[node]:
            if visited[_node] != 1:

                # 부모 저장
                parent[_node] = node

                # 큐 추가
                queue.append(_node)

    # 정답 출력
    for p in parent[2:]:
        print(p)

def dfs(size, tree, node):
    # 스택 초기화
    queue = [node]

    # 부모 저장공간 초기화
    parent = [0] * (size+1)

    # 방문 저장곤간 초기화
    visited = [0] * (size+1)

    # 스택이 비워질 때 까지 반복
    while not len(queue) == 0:
        node = queue.pop()

        # 방문 처리
        visited[node] = 1 

        # DFS
        for _node in tree[node]:
            if visited[_node] != 1:

                # 부모 저장
                parent[_node] = node

                # 큐 추가
                queue.append(_node)

    # 정답 출력
    for p in parent[2:]:
        print(p)
# -------------------------------


# Please write the code below ---
def main():
    size = int(ip())
    tree = [[] for _ in range(size+1)]

    for _ in range(size-1):
        x, y = mv(int)
        tree[x].append(y)
        tree[y].append(x)

    print(tree)

    dfs(size, tree, 1)
# -------------------------------


# Ignore it ---------------------
if __name__ == "__main__":
    main()
# -------------------------------