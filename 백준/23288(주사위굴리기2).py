N, M, K = map(int, input().split())
graph = [[0] * M for i in range(N)]
for i in range(N):
    graph[i] = list(map(int, input().split()))

dice = [[0,2,0],
        [4,1,3],
        [0,5,0],
        [0,6,0]]

dr = [1,-1,0,0]
dc = [0,0,1,-1]

score = 0 # 최종 점수

def update_dice(direct):
    global dice, graph
    # 주사위 모든 방향 저장
    r = dice[1][2]
    u = dice[1][1]
    l = dice[1][0]
    b = dice[0][1]
    i = dice[2][1]
    d = dice[3][1]

    # 동
    if direct == 0:
        dice = [[0,b,0],
                [d,l,u],
                [0,i,0],
                [0,r,0]]

    # 남
    if direct == 1:
        dice = [[0, d, 0],
                [l, b, r],
                [0, u, 0],
                [0, i, 0]]

    # 서
    if direct == 2:
        dice = [[0, b, 0],
                [u, r, d],
                [0, i, 0],
                [0, l, 0]]

    # 북
    if direct == 3:
        dice = [[0, u, 0],
                [l, i, r],
                [0, d, 0],
                [0, b, 0]]

# 주사위 굴리기 (좌표, 방향)
def move_dice(r, c, direct):
    # 동
    if direct == 0:
        nr, nc = r, c + 1
        if nr < 0 or N <= nr or nc < 0 or M <= nc:
            nr, nc = r, c - 1 # 반대 방향
            direct = (direct + 2) % 4

    # 남
    elif direct == 1:
        nr, nc = r + 1, c
        if nr < 0 or N <= nr or nc < 0 or M <= nc:
            nr, nc = r - 1, c  # 반대 방향
            direct = (direct + 2) % 4

    # 서
    elif direct == 2:
        nr, nc = r, c - 1
        if nr < 0 or N <= nr or nc < 0 or M <= nc:
            nr, nc = r, c + 1  # 반대 방향
            direct = (direct + 2) % 4

    # 북
    elif direct == 3:
        nr, nc = r - 1, c
        if nr < 0 or N <= nr or nc < 0 or M <= nc:
            nr, nc = r + 1, c  # 반대 방향
            direct = (direct + 2) % 4

    global score
    update_dice(direct) # 주사위 굴러간 후 전개도 갱신
    dice_bottom = dice[3][1] # 주사위 밑면
    score += calculate_score(nr, nc) # 점수 계산
    direct += decide_next_direct(dice_bottom, graph[nr][nc]) # 다음 방향
    next_direct = (direct + 4) % 4

    return nr, nc, next_direct

from collections import deque
def calculate_score(r, c):
    B = graph[r][c]

    visited = [[False] * M for i in range(N)]
    visited[r][c] = True
    queue = deque()
    queue.append((r, c))
    cnt = 1 # 주사위 밑면과 동일한 칸 수

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc] and B == graph[nr][nc]:
                    visited[nr][nc] = True
                    cnt += 1
                    queue.append((nr, nc))

    return cnt * B

def decide_next_direct(A, B):
    # 시계 방향 90도
    if A > B:
        direct = 1
    # 반시계 방향 90도
    elif A < B:
        direct = -1
    # 그대로
    else:
        direct = 0

    return direct


r, c = 0, 0 # 처음 좌표
direct = 0 # 처음 방향(동쪽)
for i in range(K):
    r, c, direct = move_dice(r, c, direct)

print(score)