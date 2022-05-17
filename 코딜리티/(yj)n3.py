# 1시간 42분, 풀이 참조: https://blog.naver.com/happygals/221269696967
# 알파벳마다 등장하는 index를 저장하는 그래프 생성
def make_graph(S):
    graph = [[] for i in range(26)]
    for i, val in enumerate(S):
        graph[ord(val) - ord('A')].append(i)

    return graph

def solution(S):
    MOD = 10**9 + 7
    ans = 0
    graph = make_graph(S)
    # print(graph)

    # 알파벳 모두 조회
    for i in range(26):
        if graph[i]:
            graph[i].insert(0, -1) # 맨처음 인덱스
            graph[i].append(len(S)) # 마지막 인덱스

            for j in range(len(graph[i])):
                # 맨 처음
                if graph[i][j] == -1:
                    continue
                # 맨 마지막
                elif graph[i][j] == len(S):
                    break
                # 앞괄호 경우의수 * 뒷괄호 경우의수
                else:
                    left = graph[i][j] - graph[i][j-1]
                    right = graph[i][j+1] - graph[i][j]
                    ans += (left * right) % MOD
                    ans %= MOD

    return ans

S = 'ABAABC'
S = 'ACAX'
S = 'CODILITY'
S = 'ABC'
print(solution(S))