N, M = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(N)]

from collections import deque
import copy

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

safe_cnt = 0

# 벽 3개가 설치된 후 진행
def bfs():
    global safe_cnt
    tmp_graph = copy.deepcopy(graph)
    queue = deque()

    # 바이러스 위치 모두 큐에 저장
    for i in range(N):
        for j in range(M):
            if tmp_graph[i][j] == 2:
                queue.append((i,j))

    while queue:
        r, c = queue.popleft()

        # 상,하,좌,우 탐색
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            #  범위내 실행
            if 0 <= nr < N and 0 <= nc < M:
                if tmp_graph[nr][nc] == 0:
                    tmp_graph[nr][nc] = 2 #바이러스 전파
                    queue.append((nr,nc))

    cnt = 0

    # 안전영역 개수
    for i in range(N):
        cnt += tmp_graph[i].count(0)

    safe_cnt = max(safe_cnt, cnt) # 벽3개를 설치한 조건 중에서 안전영역이 가장 큰 값

def make_wall(cnt):
    if cnt == 3:
        bfs()
        return
    else:
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 0:
                    graph[i][j] = 1 # 벽 설치
                    make_wall(cnt + 1)
                    graph[i][j] = 0 # 벽 해제

make_wall(0) # 벽 0개일 떄 실행
print(safe_cnt)