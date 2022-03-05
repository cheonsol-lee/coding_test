n = int(input())
q1, q2 = map(int, input().split())
m = int(input())

graph = [[] for i in range(n+1)]
for i in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
    
visited = [False for i in range(n+1)]
distance = [0] * (n+1) # 촌수 계산

from collections import deque
def bfs(graph, start, visited):
    global distance
    queue = deque([start])
    visited[start] = True
    
    while queue:
        start = queue.popleft()
        
        for i in graph[start]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                distance[i] = distance[start] + 1
                
                if q2 == i:
                    return True
                
    return False

is_possible = bfs(graph, q1, visited)
if is_possible:
    print(distance[q2])
else:
    print(-1)