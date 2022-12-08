from collections import defaultdict

# Breadth First Search
def bfs(vertex, graph, visited=[], queue=[]):
    visited.append(vertex)
    queue.append(vertex)
    
    while len(queue) != 0:
        data = queue.pop(0)
        print(data, end = ' ') 
        
        for neighborhood in graph[data]:
            if neighborhood not in visited:
                visited.append(neighborhood)
                queue.append(neighborhood)
                
# Depth First Search
def dfs(vertex, graph, visited=[]):
    if vertex not in visited:
        visited.append(vertex)
        print(vertex, end = ' ')  

        for neighborhood in graph[vertex]:
            dfs(neighborhood, graph, visited)

def main():
    # input
    N, M, V = map(int, input().split())

    # init graph
    graph = defaultdict(list)
    for _ in range(M):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
        graph[s].sort()
        graph[e].sort()
        
    # solve
    dfs(V, graph)
    print()
    bfs(V, graph)
    
if __name__ == '__main__':
    main()
