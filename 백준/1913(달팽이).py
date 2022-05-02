# 출처: https://egg-money.tistory.com/85 [완숙의 블로그]
# 1. 가면서 못가는 곳이 있을때 방향을 바꾼다.
# 2. 제약 조건을 설계하는데 있어 반대방향으로 가는게 좋다. while(now_num > 0)
# 3. 벽은 x < 0, x >= n, y < 0, y >= n, 그리고 방안에 들어가 있는 값이 0이 아닐 경우 벽으로 간주한다.
# 4. 벽에 부딪혔을 때, 방향을 바꾸는데, 이 순서를 0, 1, 2, 3으로 설정해두고 바꾼다.
# 5. 거꾸로 시작했으므로 아래, 오른쪽, 위, 왼쪽 이 반복될 것

N = int(input())
M = int(input())
snail = [[0] * N for i in range(N)]
move = [(1,0), (0,1), (-1,0), (0,-1)]
d = 0
r, c = (0, 0)
num = N * N

# 거꾸로 수를 채움
while(num > 0):
    snail[r][c] = num
    nr = r + move[d][0]
    nc = c + move[d][1]

    # 벽 또는 채워진 수를 만나면 방향 바꿈
    if 0 <= nc < N and 0 <= nr < N and snail[nr][nc] == 0:
        pass
    else:
        d = (d + 1) % 4
        nr = r + move[d][0]
        nc = c + move[d][1]

    (r, c) = (nr, nc)
    num -= 1

for i in range(N):
    for j in range(N):
        if snail[i][j] == M:
            find_r = i
            find_c = j
        print(snail[i][j], end=' ')
    print()

print(find_r + 1, find_c + 1)