N, K = map(int, input().split())
graph = [[] for i in range(100001)]

for i in range(100001):
    if (i-1) >= 0:
        graph[i].append(i-1)
    if ((i+1) <= 100000):
        graph[i].append(i+1)
    if ((i*2) <= 100000):
        graph[i].append(i*2)
    
visited = [False for i in range(100001)]
distance = [0 for i in range(100001)]

from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
#     visited[start] = True
    
    while queue:
        start = queue.popleft()
        
        for i in graph[start]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                distance[i] = distance[start] + 1 # start노드로부터의 거리 저장
                
                # 목적지를 찾았다면
                if i == K:
                    return distance[i]
                

if N==K:
    print(0)
else:
    count = bfs(graph, N, visited)
    print(count)