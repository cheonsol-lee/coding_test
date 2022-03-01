N, E = map(int, input().split())
height_list = list(map(int, input().split()))

height_list.insert(0, 0) # 0번은 사용 안함

# 방향성있는 인접행렬
adj_matrix = [[0 for i in range(N+1)] for j in range(N+1)]

for i in range(E):
    n1, n2 = map(int, input().split())
    
    # n1의 높이 < n2의 높이
    if height_list[n1] < height_list[n2]:
        adj_matrix[n1][n2] = 1
    # n1의 높이 > n2의 높이
    else:
        adj_matrix[n2][n1] = 1
        
# 메모이제이션
memo = [0 for i in range(N+1)]

def visit(node):
    global memo
    max_count = 0
    
    if memo[node] != 0:
        return memo[node]
    
    # 리스트에 1이 없다면
    if not (1 in adj_matrix[node]):
        memo[node] = 1
        return 1
 
    for next_node in range(1, N+1):
        if adj_matrix[node][next_node] == 0:
            continue
        
        cur_count = visit(next_node) + 1
        max_count = max(cur_count, max_count)
        
    memo[node] = max_count
        
    return max_count

for node in range(1, N+1):
    visit(node)

for i in range(1, N+1):
    print(memo[i])