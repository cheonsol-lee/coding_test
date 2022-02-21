import numpy as np

N = int(input())

# 인덱스(학생 번호)별로 좋아하는 사람 목록, 0번은 없으므로 비움
like_list = [0 for i in range(N*N + 1)] 

order_list = [] # 학생 자리 지정 순서
for i in range(N*N):
    input_list = list(map(int, input().split()))
    order_list.append(input_list[0])
    like_list[input_list[0]] = input_list[1:]
    
# 전역변수: 데이터 저장
data_map = np.array([[0 for i in range(N+1)] for j in range(N+1)]) # 학생 지정 자리 저장

# 전역변수: 데이터 조회 유무
check_map = np.array([])
for i in range(N+1):
    for j in range(N+1):
        if i==0 or j==0:
            check_map = np.append(check_map, [0]) # 조회 함 (0행 또는 0열의 위치는 0으로 표기)
        else:
            check_map = np.append(check_map, [1]) # 조회 안함            
check_map = np.reshape(check_map, (N+1,N+1))

# 전역변수: 인접 위치에 좋아하는 학생 수
count_like_map = np.array([[0 for i in range(N+1)] for j in range(N+1)]) 

# 전역변수: 인접 위치에 빈 자리 수 
count_vacant_map = np.array([[0 for i in range(N+1)] for j in range(N+1)])  

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
            
# 문제 조건처리 함수
def problem_condition():
    global data_map, check_map, count_like_map, count_vacant_map
    
    # condition1
    if(sum(np.ravel(count_like_map, order='C')) == 0):
        tmp = check_map + count_like_map
    else:
        tmp = check_map * count_like_map 
    
    # 좋아하는 학생 맵과 check 맵이 겹치지 않는 경우
    if(sum(np.ravel(tmp, order='C')) == 0):
        tmp = check_map
    
    # 원소 개수 == 1
    if(np.count_nonzero(np.ravel(tmp, order='C') != 0) == 1):
        final_index = np.where(np.ravel(tmp, order='C') != 0)[0][0]
#         print('condition 1')
        return final_index
    
    # condition2
    tmp2 = tmp * count_vacant_map
    if(sum(np.ravel(tmp2, order='C')) == 0):
        # 원소가 모두 0일 때
        # 좋아하는 학생이 인접한 칸과 빈자리가 인접한 칸이 겹치지 않는 경우
        tmp2 = tmp 

    # 원소 개수 == 1
    if(np.count_nonzero(np.ravel(tmp2, order='C') != 0) == 1):
        final_index = np.where(np.ravel(tmp2, order='C') != 0)[0][0]
#         print('condition 2')
        return final_index
    
    # condition3
    final_index = np.argmax(tmp2)
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
satis_list = np.ravel(count_like_map, order='C')
number, count = np.unique(satis_list, return_counts=True)
satis_dict = dict(zip(number, count)) # 학생별 만족도 수치 dictionary

# 만족도 조건사항
number = np.array([0,1,2,3,4])
point = np.array([0,1,10,100,1000])
score_dict = dict(zip(number, point)) # 만족도 조건 dictionary

final_point = 0
for i in satis_dict:
    final_point += satis_dict[i] * score_dict[i]
    
print(final_point)