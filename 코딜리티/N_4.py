def solution(A):
    cnt = 0
    max_cnt = 0
    sign_arr = [0] * len(A) # 부호 저장

    # 맨 처음에 0이 등장했을 때, 처리
    if A[0] == 0:
        if A[1] > 0:
            sign_arr[0] = '-'
        if A[1] < 0:
            sign_arr[0] = '+'

    # 부호 붙이기
    for i in range(0, len(A)):
        if A[i] > 0:
            sign_arr[i] = '+'
        if A[i] < 0:
            sign_arr[i] = '-'

        # 중간에 0이 등장했을 때, 처리
        if A[i] == 0 and i != 0:
            if sign_arr[i-1] =='+':
                sign_arr[i] = '-'
            else:
                sign_arr[i] = '+'

    # 가장 긴 배열 찾기 (+,-) 또는 (-,+) 쌍 개수 찾기
    for i in range(0, len(A)-1):
        if sign_arr[i] == '+' and sign_arr[i+1] == '-':
            cnt += 1
        elif sign_arr[i] == '-' and sign_arr[i+1] == '+':
            cnt += 1
        else:
            cnt = 0

        max_cnt = max(max_cnt, cnt)

    print(sign_arr)
    if max_cnt == 0:
        return max_cnt
    else:
        return max_cnt+1 # (+,-) 또는 (-,+)는 항상 쌍으로 존재



A = [5, 4, -3, 2, 0, 1, -1, 0, 2, -3, 4, -5]
A = [1,0,-1]
A = [1,1,1,1,0,1,1,-1]
A = [-1,-1,-1,0]
A = [-1,-1,-1]
print(solution(A))