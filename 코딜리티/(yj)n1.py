# 20분
def solution(A):
    before = A[0]
    cnt = 1
    max_index = 0
    max_cnt = 0
    start = 0
    for i in range(1, len(A)):
        if before < A[i]:
            cnt += 1
            before = A[i]
        else:
            if max_cnt < cnt:
                max_cnt = max(max_cnt, cnt)
                max_index = start

            cnt = 1
            before = A[i]
            start = i

    if max_cnt < cnt:
        max_cnt = max(max_cnt, cnt)
        max_index = start

    return max_index


# A = [2,2,2,2,1,2,-1,2,1,3]
A = [30,20,10,20,30,1,2,3,4]
print(solution(A))