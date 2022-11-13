from collections import deque

def bfs (graph, node, visited):
    queue = deque([node])
    visited[node] = True

    print('visited -> ', visited)
    
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not (visited[i]):
                queue.append(i)
                visited[i] = True


def main():
    m, n = map(int, input().split())

    print(f'm = {m}, n = {n}')

    graph = []
    for _ in range(0, n):
        x = list(map(int, input().split()))
        graph.append(x)

    print(f'graph = {graph}')

    visited = [False] * (n+1)

    bfs(graph, 1, visited)

if __name__ == "__main__":
    main()