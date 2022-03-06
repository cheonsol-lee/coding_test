# 세로
def vertical_check(i,j,num):
    count = 0
    for k in range(5):
        if (i+k)<19:
            if data[i+k][j] == num:
                count += 1
    if count == 5:
        # 육목이면 False
        if i-1 >= 0:
            if data[i-1][j] == num:
                return False
            
        # 육목이면 False
        if i+5 < 19:
            if data[i+5][j] == num:
                return False
            else:
                return True
        else:
            return True
    else:
        return False

# 가로
def horizontal_check(i,j,num):
    count = 0
    for k in range(5):
        if (j+k)<19:
            if data[i][j+k] == num:
                count += 1
                
    if count == 5:
        # 육목이면 False
        if j-1 >= 0:
            if data[i][j-1] == num:
                return False
        
        # 육목이면 False
        if j+5 < 19:
            if data[i][j+5] == num:
                return False
            else:
                return True
        else:
            return True
    else:
        return False

# 대각선(오른쪽-아래)
def diagonal_check_down(i,j,num):
    count = 0
    for k in range(5):
        if (i+k)<19 and (j+k)<19:
            if data[i+k][j+k] == num:
                count += 1
    if count == 5:
        # 육목이면 False
        if i-1 >= 0 and j-1 >= 0:
            if data[i-1][j-1] == num:
                return False
        
        # 육목이면 False
        if i+5 < 19 and j+5 < 19:
            if data[i+5][j+5] == num:
                return False
            else:
                return True
        else:
            return True
    else:
        return False

# 대각선(오른쪽-위)
def diagonal_check_up(i,j,num):
    count = 0
    for k in range(5):
        if (i-k)>=0 and (j+k)<19:
            if data[i-k][j+k] == num:
                count += 1
    if count == 5:
        # 육목이면 False
        if i+1 < 19 and j-1 >= 0:
            if data[i+1][j-1] == num:
                return False
        
        # 육목이면 False
        if i-5 >= 0 and j+5 < 19:
            if data[i-5][j+5] == num:
                return False
            else:
                return True
        else:
            return True
    else:
        return False
    
data = [[0 for i in range(19)] for j in range(19)]

for i in range(19):
    data[i] = (list(map(int, input().split())))

num = 0
token = False

for i in range(19):
    for j in range(19):
        if data[i][j] == 0:
            continue
        
        # 검은색 체크
        if data[i][j] == 1:
            if vertical_check(i,j,1) or horizontal_check(i,j,1) or diagonal_check_down(i,j,1) or diagonal_check_up(i,j,1):
                num = 1
                token = True
                break
        
        # 흰색 체크
        if data[i][j] == 2:
            if vertical_check(i,j,2) or horizontal_check(i,j,2) or diagonal_check_down(i,j,2) or diagonal_check_up(i,j,2):
                num = 2
                token = True
                break
    
    if token == True:
        break

# 승리가 결정될 때
if token==True:
    print(num)
    print(i+1, j+1)
else:
    print(0)