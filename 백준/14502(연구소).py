# 참조: https://hongcoding.tistory.com/m/130
from collections import deque
import copy

def bfs():
    queue = deque()
    tmp_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            # 바이러스인 것을 queue에 넣음
            if tmp_graph[i][j] == 2:
                queue.append((i, j))

    # 바이러스가 퍼질 수 있는 공간은 모두 2로 변경
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                queue.append((nx, ny))

    global answer
    cnt = 0

    # 바이러스가 퍼지지 않은 지역의 개수 세기
    for i in range(n):
        cnt += tmp_graph[i].count(0)

    answer = max(answer, cnt)

# 벽 만들기 함수
def make_wall(cnt):
    # 벽 3개를 지으면 bfs 실행
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt+1)
                graph[i][j] = 0

n, m = map(int, input().split())
graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    graph.append(list(map(int, input().split())))

answer = 0
make_wall(0)
print(answer)

