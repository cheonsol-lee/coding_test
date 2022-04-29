# 출처: https://wlstyql.tistory.com/72
N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
from collections import deque
queue = deque()
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def pos_init():
    rr, rc, br, bc = 0, 0, 0, 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'R':
                rr, rc = i, j
            elif graph[i][j] == 'B':
                br, bc = i, j

    # 위치정보와 depth
    queue.append((rr, rc, br, bc, 1))
    visited[rr][rc][br][bc] = True

def move(r, c, dr, dc):
    cnt = 0 # 이동 칸수
    # 다음이 벽 또는 현재가 구멍일 때까지
    while graph[r + dr][c + dc] != '#' and graph[r][c] != 'O':
        r += dr
        c += dc
        cnt += 1
    return r, c, cnt


def solve():
    pos_init()
    while queue:
        rr, rc, br, bc, depth = queue.popleft()

        # 실패 조건
        if depth > 10:
            break
        # 4방향 탐색
        for i in range(4):
            nrr, nrc, rcnt = move(rr, rc, dr[i], dc[i])
            nbr, nbc, bcnt = move(br, bc, dr[i], dc[i])

            # 실패 조건이 아니라면
            if graph[nbr][nbc] != 'O':
                # 성공조건
                if graph[nrr][nrc] == 'O':
                    print(depth)
                    return
                # R, B 겹칠 때
                if (nrr, nrc) == (nbr, nbc):
                    # 이동거리가 많은 것을 한칸 뒤로
                    if rcnt > bcnt:
                        nrr -= dr[i]
                        nrc -= dc[i]
                    else:
                        nbr -= dr[i]
                        nbc -= dc[i]

                # 너비 기반 탐색 체크
                if not visited[nrr][nrc][nbr][nbc]:
                    visited[nrr][nrc][nbr][nbc] = True
                    queue.append((nrr, nrc, nbr, nbc, depth + 1))

    print(-1)

solve()