def solution(A):
    local_max = A[0]
    global_max = A[0]

    # 이전까지의 최대합(local_max)와 뒤의 값(A[i])의 합, 뒤의 값(A[i]) => 최대값 저장
    for i in range(1, len(A)):
        local_max = max(A[i], local_max + A[i])
        global_max = max(global_max, local_max)

    return global_max

A = [1,2,3,-1,-5,7,-3,5]
# A = [3,2,-6,4,0]
# A = [14,-6,8,-15,17]
# A = [-10]
# A = [-10,1]
# A = [-10,-1]
A = [-10,-1,-3]
print(solution(A))