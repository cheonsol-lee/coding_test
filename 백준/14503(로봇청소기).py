N, M = map(int, input().split())
r, c, d = map(int,input().split()) # 0(북), 1(동), 2(남), 3(서)
d = 3-d # 방향 보정 # 0(서), 1(남), 2(동), 3(북)
graph = [list(map(int, input().split())) for i in range(N)] #0(빈칸), 1(벽), 2(청소완료)

# 방향: 서, 남, 동, 북
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]
cnt = 0 #청소 횟수
def dfs(r, c, d):
    global cnt, graph
    if graph[r][c] == 0:
        cnt += 1
        graph[r][c] = 2 # 청소 위치


    for i in range(1,5):
        nd = (d + i) % 4 # 왼쪽 방향(270도 회전)
        nr = r + dr[nd]
        nc = c + dc[nd]

        # 테두리 범위 내 위치
        if 0<nr<N-1 and 0<nc<M-1:
            # 아직 청소안된 곳 (방문 안한 곳)
            if graph[nr][nc] == 0:
                dfs(nr, nc, nd)
                return # 원래로 돌아가는 것이 아니라 한번 dfs로 끝내기

    # 모두 갈 수 없으면 후진
    nd = (d + 2) % 4
    nr = r + dr[nd]
    nc = c + dc[nd]
    # 후진 방향이 벽이라면 중지
    if graph[nr][nc] == 1:
        return
    dfs(nr, nc, d) # 후진할 때도, 방향은 그대로

dfs(r, c, d)
print(cnt)
