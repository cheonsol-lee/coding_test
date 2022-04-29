N, M = map(int, input().split())
graph = [list(input()) for i in range(N)]
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
from collections import deque
queue = deque()
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def init():
    rr, rc, br, bc = 0, 0, 0, 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'R':
                rr, rc = i, j
            if graph[i][j] == 'B':
                br, bc = i, j
    # 위치좌표, depth
    queue.append((rr, rc, br, bc, 1))

def move(r, c, dr, dc):
    cnt = 0
    while graph[r + dr][c + dc] != '#' and graph[r][c] !='O':
        r += dr
        c += dc
        cnt += 1
    return r, c, cnt

def solve():
    init()
    while queue:
        rr, rc, br, bc, depth = queue.popleft()
        # 실패조건
        if depth > 10:
            break
        for i in range(4):
            nrr, nrc, rcnt = move(rr, rc, dr[i], dc[i])
            nbr, nbc, bcnt = move(br, bc, dr[i], dc[i])

            # 실패 조건이 아닐때
            if graph[nbr][nbc] != 'O':
                if graph[nrr][nrc] == 'O':
                    print(1)
                    return
                if (nrr, nrc) == (nbr, nbc):
                    if rcnt > bcnt:
                        nrr -= dr[i]
                        nrc -= dc[i]
                    else:
                        nbr -= dr[i]
                        nbc -= dc[i]
                if not visited[nrr][nrc][nbr][nbc]:
                    visited[nrr][nrc][nbr][nbc] = True
                    queue.append((nrr, nrc, nbr, nbc, depth + 1))
    print(0)

solve()