N = int(input())
data_map = [list(map(int, input().split())) for _ in range(N)]    
dx = [-1,1,0,0,0]
dy = [0,0,-1,1,0]

min_cost = 987654321 # 최소 가격 지정
sum_list = []
seed_list = []
for i in range(1,N-1):
    for j in range(1,N-1):
        cost = 0 # 비용
        
        for k in range(5):
            nx = i + dx[k]
            ny = j + dy[k]
            
            cost += data_map[nx][ny]
        
        sum_list.append(cost)
        seed_list.append((i,j))
        
# 상하좌우, 대각선, 상하좌우 2칸씩 띄기
ban_condition_x = [0, -1,-1,-1,0,0,1,1,1, -2,0,0,2]
ban_condition_y = [0, -1,0,1,-1,1,-1,0,1, 0,-2,2,0]

def ban_confirm(seed_1, seed_2):
    x = seed_1[0]
    y = seed_1[1]
    
    for z in range(13):
        nx = x + ban_condition_x[z]
        ny = y + ban_condition_y[z]
#         print((nx,ny))
        if (nx,ny) == seed_2:
            return False # 하나라도 충돌이 있으면 False
        else:
            continue
            
    return True # 모두 충돌하지 않는다면 True

length = len(seed_list)
min_cost = 1001

for i in range(0, length-2):
    for j in range(i+1, length-1):
        for k in range(j+1, length):
            # i,j,k 가 가능한 조합인지 파악
            seed_1 = seed_list[i]
            seed_2 = seed_list[j]
            seed_3 = seed_list[k]
            
            # 모두 True 일 때, 3가지 씨앗이 가능한 경우이므로 최소 비용 저장
            if(ban_confirm(seed_1, seed_2) and ban_confirm(seed_1, seed_3) and ban_confirm(seed_2, seed_3)):
                cost = sum_list[i] + sum_list[j] + sum_list[k]

                # 최소 비용 저장
                if cost < min_cost:
                    min_cost = cost

print(min_cost)