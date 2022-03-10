N, M, V = map(int, input().split())
graph = [[] for i in range(N + 1)]

for i in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# 방문할 수 있는 정점이 여러 개인 경우
# 정점 번호가 작은 것을 먼저 방문   
for i in range(1, N+1):
    graph[i].sort()
    
visited_dfs = [False for i in range(N + 1)]
visited_bfs = [False for i in range(N + 1)]

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    
    
from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    print(start, end=' ')
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                print(i, end=' ')
            
            
dfs(graph, V, visited_dfs)
print()
bfs(graph, V, visited_bfs)


