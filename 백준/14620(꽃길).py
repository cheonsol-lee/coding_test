import sys
input = sys.stdin.readline
N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

visited = [[False] * N for i in range(N)]
dr = [-1, 1, 0, 0, 0]
dc = [0, 0, -1, 1, 0]
min_sum = 987654321

# 범위 체크
def check(r, c):
    for i in range(5):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == False:
            continue
        else:
            return False
    return True

# 꽃이 펼쳐지는 지역의 합
def calculate(r, c):
    tmp_sum = 0
    for i in range(5):
        nr = r + dr[i]
        nc = c + dc[i]
        tmp_sum += graph[nr][nc]
    return tmp_sum

def make_seed(cost, cnt):
    global min_sum
    if cnt == 3:
        # 씨앗 위치의 최소합 구하기
        min_sum = min(min_sum, cost)
        return
    else:
        for r in range(1, N-1):
            for c in range(1, N-1):
                if check(r, c):
                    for i in range(5):
                        nr = r + dr[i]
                        nc = c + dc[i]
                        visited[nr][nc] = True

                    make_seed(cost + calculate(r, c), cnt + 1)
                    for i in range(5):
                        nr = r + dr[i]
                        nc = c + dc[i]
                        visited[nr][nc] = False


make_seed(0, 0)
print(min_sum)v