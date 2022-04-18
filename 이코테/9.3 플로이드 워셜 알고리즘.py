'''
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 셀프 루프는 0으로 초기화
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

# 간선에 대한 정보 입력
for _ in range(m):
    i, j, k = map(int, input().split())
    graph[i][j] = k

# 점화식에 따라 플로이드 와셜 알고리즘 실행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달 불가능하면, 무한 출력
        if graph[a][b] == INF:
            print('INFINITY', end = ' ')
        else:
            print(graph[a][b], end = ' ')

    print()