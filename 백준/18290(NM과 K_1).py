N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
check_arr = [[False] * M for i in range(N)] # K 칸 기록용
max_val = -1000000
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def select_loc(pr, pc, cnt, cur_val):
    global max_val
    if cnt == K:
        if max_val < cur_val:
            max_val = cur_val
        return
    else:
        for r in range(pr, N):
            for c in range(pc if r==pr else 0, M):
                # 이미 선택된 칸
                if check_arr[r][c] == 1:
                    continue

                token = True # 인접칸을 이미 선택했다면 False

                # 인접칸 체크
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if 0 <= nr < N and 0 <= nc < M:
                        # 인접 칸이 이미 선택되었다면 False
                        if check_arr[nr][nc]:
                            token = False

                if token:
                    check_arr[r][c] = True
                    select_loc(r, c, cnt + 1, cur_val + arr[r][c])
                    check_arr[r][c] = False


select_loc(0, 0, 0, 0)
print(max_val)