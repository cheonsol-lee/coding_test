import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력
n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1) # 최단거리 테이블

for _ in range(m):
    # a노드 -> b노드 : 비용 c
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드 번호
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단거리가 짧은 노드 인덱스
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0 # 시작노드 초기화
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1] # 노드별 거리 입력

    # 시작 노드 제외한 전체 n - 1개 노드 반복
    for i in range(n - 1):
        now = get_smallest_node() # 현재 최단 거리가 가장 짧은 노드
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]

            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

# 출발 노드부터 모든 노드에 대한 최단 거리 출력
for i in range(1, n + 1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])

