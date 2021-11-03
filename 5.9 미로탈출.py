from collections import deque

N, M = map(int, input().split())

graph = list()
for i in range(N):
    graph.append(list(map(int, input())))

# 이동방향
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 미로 벗어날 경우
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            # 벽일 경우
            if graph[nx][ny]==0:
                continue
            # 방문하지 않은 곳만 최단 거리 기록
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    
    # 오른쪽 맨 하단의 값 출력
    return graph[N-1][M-1]

print(bfs(0,0))