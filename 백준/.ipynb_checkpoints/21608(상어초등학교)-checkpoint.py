N = int(input())
like_list = [0 for i in range(N*N + 1)] # 인덱스(학생 번호)별로 좋아하는 사람 목록, 0번은 없으므로 비움

order_list = [] # 학생 자리 지정 순서
for i in range(N*N):
    input_list = list(map(int, input().split()))
    order_list.append(input_list[0])
    like_list[input_list[0]] = input_list[1:]
    
# 전역변수: 데이터 저장
data_map = [[0 for i in range(N+1)] for j in range(N+1)] # 학생 지정 자리 저장

# 전역변수: 데이터 조회 유무
check_map = [[0 for i in range(N+1)] for j in range(N+1)]
for i in range(N+1):
    for j in range(N+1):
        if i==0 or j==0:
            check_map[i][j] = 0 # 조회 함 (0행 또는 0열의 위치는 0으로 표기)
        else:
            check_map[i][j] = 1 # 조회 안함         
            
# 전역변수: 인접 위치에 좋아하는 학생 수
count_like_map = [[0 for i in range(N+1)] for j in range(N+1)]

# 전역변수: 인접 위치에 빈 자리 수 
count_vacant_map = [[0 for i in range(N+1)] for j in range(N+1)]

# 자리계산 또는 만족도 계산용
def count_like_and_vacant_map(num, satisfaction=False):
    global data_map, check_map, count_like_map, count_vacant_map
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for i in range(1, N+1):
        for j in range(1, N+1):
            # 만족도 함수용으로 사용할 때
            if satisfaction:
                num = data_map[i][j]
            
            count_like = 0 # 인접 칸의 좋아하는 학생 수
            count_vacant = 0 # 인접 칸의빈칸 수

            # 인접 칸 탐색
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]

                # 데이터 범위 벗어나면 무시
                if(ni>N or ni<1 or nj>N or nj<1):
                    continue

                adj_num = data_map[ni][nj] # 인접 칸의 좋아하는 학생 번호

                # 자리를 배치할 학생 번호(num)의 선호 리스트에 있는지 조회
                count_like   += adj_num in like_list[num] # 인접 칸의 좋아하는 학생 수 합
                count_vacant += check_map[ni][nj] == 1 # 인접 칸의 빈자리 수 합

            count_like_map[i][j]   = count_like # 좋아하는 학생 수 기록
            count_vacant_map[i][j] = count_vacant # 빈칸 수 기록
            
def sum_2_list(lst):
    return sum([sum(lst[i]) for i in range(N+1)])

def flatten_2_list(lst):
    return [lst[i][j] for i in range(N+1) for j in range(N+1)]

def count_nonzero_element_list(lst):
    count = 0
    for element in lst:
        if element != 0:
            count += 1
    return count

def first_time_nonzero_index(lst):
    final_index = -1
    for index, i in enumerate(lst):
        if i != 0:
            final_index = index
            break
    return final_index

# 문제 조건처리 함수
def problem_condition():
    global data_map, check_map, count_like_map, count_vacant_map
    
    # 1차원 리스트로 변경
    check_map_list = flatten_2_list(check_map)
    count_like_map_list = flatten_2_list(count_like_map)
    count_vacant_map_list = flatten_2_list(count_vacant_map)
    
    # condition1
    if(sum(count_like_map_list) == 0):
        tmp = [x + y for x, y in zip(check_map_list, count_like_map_list)] # 두 1차원 리스트 간의 합
    else:
        tmp = [x * y for x, y in zip(check_map_list, count_like_map_list)]
    
    # check_map과 count_like_map이 겹치는게 없을 때
    if(sum(tmp) == 0):
        tmp = check_map_list.copy()
    
    # 원소 개수 == 1
    if(count_nonzero_element_list(tmp) == 1):
        final_index = first_time_nonzero_index(tmp)
#         print('condition 1')
        return final_index
    
    # condition2
    tmp2 = [x * y for x, y in zip(tmp, count_vacant_map_list)]
    if(sum(tmp2) == 0):
        # 원소가 모두 0일 때
        # 좋아하는 학생이 인접한 칸과 빈자리가 인접한 칸이 겹치지 않는 경우
        tmp2 = tmp.copy()

    # 원소 개수 == 1
    if(count_nonzero_element_list(tmp2) == 1):
        final_index = first_time_nonzero_index(tmp2)
#         print('condition 2')
        return final_index
    
    # condition3
    tmp2_max = max(tmp2)
    final_index = tmp2.index(tmp2_max)
#     print('condition 3')
    return final_index

# solve1 : 자리 배치
for stu_id in order_list:
#     print(stu_id)
    count_like_and_vacant_map(stu_id)
    final_index = problem_condition()
    
    # 최종의 행, 열
    fi = final_index // (N + 1)# 행
    fj = final_index % (N + 1) # 열
    
    data_map[fi][fj] = stu_id # 자리 배치 기록
    check_map[fi][fj] = 0 # 조회 기록
    
# solve2 : 만족도 계산
count_like_and_vacant_map(num=-1, satisfaction=True)
satis_list = flatten_2_list(count_like_map)

numbers = [1,2,3,4]
cnt_1 = 0
cnt_2 = 0
cnt_3 = 0
cnt_4 = 0

for i in satis_list:
    if i == 1:
        cnt_1 += 1
    elif i == 2:
        cnt_2 += 1
    elif i == 3:
        cnt_3 += 1
    elif i == 4:
        cnt_4 += 1
        
counts = [cnt_1, cnt_2, cnt_3, cnt_4]
satis_dict = dict(zip(numbers, counts)) # 학생별 만족도 수치 dictionary

# 만족도 조건사항
points = [1,10,100,1000]
score_dict = dict(zip(numbers, points)) # 만족도 조건 dictionary

final_point = 0
for i in satis_dict:
    final_point += satis_dict[i] * score_dict[i]
    
print(final_point)