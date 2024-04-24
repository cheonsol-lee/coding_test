N, M, r, c, K = map(int, input().split())
graph = [[-1]*M for i in range(N)] # 지도
for i in range(N):
    graph[i] = list(map(int, input().split()))
directions = list(map(int, input().split())) # 방향 순서

dice = [[-1, 0, -1],
        [ 0, 0,  0],
        [-1, 0, -1],
        [-1, 0, -1]]

# 방향 d로 주사위 굴리기
def move_dice(direction, nr, nc):
    global graph, dice
    l = dice[1][0]  # 왼쪽
    r = dice[1][2]  # 오른쪽
    u = dice[1][1]  # 위쪽
    d = dice[3][1]  # 아래쪽
    i = dice[2][1]  # 앞쪽
    b = dice[0][1]  # 뒤쪽

    # 동(1)
    if direction == 1:
        if graph[nr][nc] != 0:
            r = graph[nr][nc]
            graph[nr][nc] = 0
        else:
            graph[nr][nc] = r
        dice = [[0,b,0],
                [d,l,u],
                [0,i,0],
                [0,r,0]]
        print(l)

    # 서(2)
    if direction == 2:
        if graph[nr][nc] != 0:
            l = graph[nr][nc]
            graph[nr][nc] = 0
        else:
            graph[nr][nc] = l
        dice = [[0,b,0],
                [u,r,d],
                [0,i,0],
                [0,l,0]]
        print(r)

    # 북(3)
    if direction == 3:
        if graph[nr][nc] != 0:
            b = graph[nr][nc]
            graph[nr][nc] = 0
        else:
            graph[nr][nc] = b
        dice = [[0,u,0],
                [l,i,r],
                [0,d,0],
                [0,b,0]]
        print(i)

    # 남(4)
    if direction == 4:
        if graph[nr][nc] != 0:
            i = graph[nr][nc]
            graph[nr][nc] = 0
        else:
            graph[nr][nc] = i
        dice = [[0,d,0],
                [l,b,r],
                [0,u,0],
                [0,i,0]]
        print(b)

# 좌표(r, c)에서 direction 방향으로 갈 수 있는지 체크
def check(r, c, direction):
    # 동(1)
    if direction == 1:
        nr, nc = r, c+1
        if 0 <= nr < N and 0 <= nc < M:
            return nr, nc
        else:
            return -1, -1

    # 서(2)
    if direction == 2:
        nr, nc = r, c-1
        if 0 <= nr < N and 0 <= nc < M:
            return nr, nc
        else:
            return -1, -1

    # 북(3)
    if direction == 3:
        nr, nc = r-1, c
        if 0 <= nr < N and 0 <= nc < M:
            return nr, nc
        else:
            return -1, -1

    # 남(4)
    if direction == 4:
        nr, nc = r+1, c
        if 0 <= nr < N and 0 <= nc < M:
            return nr, nc
        else:
            return -1, -1


for direction in directions:
    nr, nc = check(r, c, direction)

    # 다음 방향이 범위 밖이라면
    if nr == -1:
        continue
    else:
        move_dice(direction, nr, nc)
        r, c = nr, nc