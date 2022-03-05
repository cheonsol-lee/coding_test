N = int(input())
data_map = [[0 for i in range(N)] for j in range(N)]

max_value = 0
for i in range(N):
    one_list = list(map(int, input().split()))

    max_value = max(max_value, max(one_list))
    data_map[i] = one_list
    
# check_map = [[1 for i in range(N)] for j in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x, y, h):
    global data_map, check_map
    
    if x<=-1 or x>=N or y<=-1 or y>=N:
        return False
    
    # 아직 방문하지 않았다면
    if check_map[x][y] > h:
        check_map[x][y] = h
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            dfs(nx, ny, h)
        return True
    
    return False

import copy 
max_count = 0

for h in range(max_value):
    check_map = copy.deepcopy(data_map)
    count = 0
    
    for x in range(N):
        for y in range(N):
            if dfs(x,y,h) == True:
                count += 1
            max_count = max(max_count, count)
            
            
print(max_count)