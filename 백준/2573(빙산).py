N, M = map(int, input().split())

data_map = [[0 for i in range(M)] for j in range(N)]
check_map = [[0 for i in range(M)] for j in range(N)]

for i in range(N):
    data_map[i] = list(map(int, input().split()))
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 빙하 덩어리 탐색용
def dfs(x, y):
    global check_map

    # 아직 방문하지 않았다면
    if check_map[x][y] >= 1:
        check_map[x][y] = 0
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            dfs(nx, ny)   
        return True
    
    return False

# 빙하 녹이기용
def melt(x, y):
    global data_map, check_map
    sea_count = 0
    
    # 아직 방문하지 않았다면
    if check_map[x][y] >= 1:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 주변이 바다라면
            if check_map[nx][ny] == 0:
                sea_count += 1
                
        data_map[x][y] -= sea_count    
        

import copy
year_count = 0 # 빙산 분리 연도

while True:
    ice_count = 0
    check_map = copy.deepcopy(data_map)
    
    # 녹이기
    for i in range(1, N-1):
        for j in range(1, M-1):
            melt(i, j)
    
    # 빙하 묶음 개수
    for i in range(1, N-1):
        for j in range(1, M-1):
            if dfs(i, j):
                ice_count += 1
    
    # 빙산 0개이면 종료
    if ice_count == 0:
        print(0)
        break

    # 빙하 2개이상이면 종료            
    if ice_count >= 2:
        print(year_count)
        break
      
    year_count += 1