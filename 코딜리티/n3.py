# 풀이시간 : 25분
# B = ['.#..#', '##..#', '...#.'] # 예상답 : [1,1,1]
B = ['.#..#', '##..#', '...#.', '##.#.'] # 예상답 : [0,3,1]
M = 5
N = 4
visited = [[False] * M for i in range(N)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]
answer = [0] * 3

from collections import deque
def bfs(r, c):
    global cnt_patrol, cnt_submarine, cnt_destroyers
    # 이미 방문했으면 종료
    if visited[r][c] == True:
        return

    queue = deque()
    queue.append((r,c))
    visited[r][c] = True
    cnt = 1 # '#'의 개수 카운트

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 범위 안에 있다면 실행
            if 0 <= nr < N and 0 <= nc < M:
                # '#'이 있고, 방문하지 않았다면 실행
                if B[nr][nc] == '#' and not visited[nr][nc]:
                    visited[nr][nc] = True
                    cnt += 1
                    queue.append((nr, nc))
    # patrol
    if cnt == 1:
        answer[0] += 1
    elif cnt == 2:
        answer[1] += 1
    else:
        answer[2] += 1

for r in range(N):
    for c in range(M):
        if B[r][c] == '#' and not visited[r][c]:
            bfs(r, c)

print(answer)