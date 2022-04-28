<<<<<<< HEAD
import sys
input = sys.stdin.readline
N = int(input())
stu_dict = dict()
graph = [[0] * N for i in range(N)]
dr = [1,-1,0,0]
dc = [0,0,1,-1]
answer = 0

for i in range(N**2):
    input_list = list(map(int, input().split()))
    stu_id = input_list[0]
    stu_like = input_list[1:]
    stu_dict[stu_id] = stu_like
    max_like_cnt = -1
    max_empty_cnt = -1

    for r in range(N):
        for c in range(N):
            if graph[r][c] == 0:
                like_cnt = 0
                empty_cnt = 0

                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if 0 <= nr < N and 0 <= nc < N:
                        if graph[nr][nc] in stu_like:
                            like_cnt += 1

                        if graph[nr][nc] == 0:
                            empty_cnt += 1

                if (max_like_cnt < like_cnt) or (max_like_cnt == like_cnt and max_empty_cnt < empty_cnt):
                    max_like_cnt = like_cnt
                    max_empty_cnt = empty_cnt
                    max_r = r
                    max_c = c

    graph[max_r][max_c] = stu_id

for r in range(N):
    for c in range(N):
        like_stu_list = stu_dict[graph[r][c]]
        cnt = 0

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if graph[nr][nc] in like_stu_list:
                    cnt += 1

        if cnt != 0:
            answer += 10 ** (cnt-1)

print(answer)
=======
print(round(0.3))
print(round(-0.7))
print(round(-0.51))
print(round(-1.4)) tsetset
>>>>>>> main
