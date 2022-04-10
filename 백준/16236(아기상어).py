# 참고: https://11001.tistory.com/96
N = int(input())
graph = [list(map(int, input().split())) for i in range(N)]
shark_r, shark_c = 0, 0 # 상어 위치 좌표
fish_cnt = 0 # 남은 물고기 수
time = 0 # 총 걸린 시간
eat_cnt = 0 # 물고기 먹은 수
shark_size = 2 # 상어 크기

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

for i in range(N):
    for j in range(N):
        # 빈칸 넘어감
        if 0 <= graph[i][j] <= 6:
            fish_cnt += 1
        elif graph[i][j] == 9:
            shark_r, shark_c = i, j
            graph[shark_r][shark_c] = 0 # 상어 위치도 0으로 변경

from collections import deque
def bfs(shark_r, shark_c):
    global shark_size, N
    queue = deque([(0, shark_r, shark_c)])
    dist_list = [] #(거리, shark_r, shark_c)
    visited = [[False] * N for i in range(N)]
    visited[shark_r][shark_c] = True

    while queue:
        dist, r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 범위내 위치 and 방문 안한 곳
            if (0 <= nr < N and 0 <= nc < N) and not visited[nr][nc]:
                # 이웃칸을 이동할 수 있는지 파악
                if graph[nr][nc] <= shark_size:
                    visited[nr][nc] = True
                    # 먹을 수 있는지 파악
                    if 0 < graph[nr][nc] < shark_size:
                        dist_list.append((dist+1, nr, nc))

                    # 물고기 위치를 하나라도 찾았으면 더이상 큐에 넣지 않기
                    if len(dist_list) == 0:
                        queue.append((dist + 1, nr, nc))

    if dist_list:
        dist_list.sort() #(거리, shark_r, shark_c) 순으로 정렬
        return dist_list[0]
    else:
        return False

while fish_cnt:
    result = bfs(shark_r, shark_c)
    if not result:
        break
    shark_r, shark_c = result[1], result[2]
    time += result[0]
    eat_cnt += 1
    fish_cnt -= 1

    # 성장 조건
    if shark_size == eat_cnt:
        shark_size += 1
        eat_cnt = 0

    graph[shark_r][shark_c] = 0

print(time)