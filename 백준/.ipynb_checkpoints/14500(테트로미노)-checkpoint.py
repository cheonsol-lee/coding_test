# 참조 : https://youtu.be/rXdmuDf9WS0
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(N)]
visited = [[False] * M for i in range(N)]
max_sum = 0 # 최대값

# 4개 방향
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, cnt, sum):
    global max_sum

    if cnt == 4:
        max_sum = max(max_sum, sum)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 안에 위치 & 방문하지 않은 경우
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, cnt+1, sum + graph[nx][ny])
            visited[nx][ny] = False

# 'ㅜ' 별도 처리
def get_last(x, y):
    base = graph[x][y] # 기준점의 값 저장
    cnt = 0
    min_val = 987654321

    # 기준점 주변의 사방 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 안에 위치
        if 0 <= nx < N and 0 <= ny < M:
            cnt += 1
            base += graph[nx][ny]
            min_val = min(min_val, graph[nx][ny]) # 4방향에서 최솟값 저장

    # 4방향 모두 탐색 가능
    if cnt == 4:
        return base - min_val

    # 3방향만 탐색 가능
    elif cnt == 3:
        return base

    # 나머지는 모양 만들기 실패
    else:
        return -1


for x in range(N):
    for y in range(M):
        visited[x][y] = True
        dfs(x, y, 1, graph[x][y]) # 'ㅜ'를 제외한 나머지 경우는 dfs로 탐색
        max_sum = max(get_last(x, y), max_sum) # 'ㅜ' 별도 처리
        visited[x][y] = False

print(max_sum)