def solution(A):
    cnt = 0
    max_cnt = 0
    for i in range(0, len(A)-1):
        if A[i] >= 0 and A[i+1] <= 0:
            cnt += 1
            print(i, cnt)
        elif A[i+1] >= 0 and A[i] <= 0:
            cnt += 1
            print(i, cnt)
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 0

    return max_cnt



A = [5, 4, -3, 2, 0, 1, -1, 0, 2, -3, 4, -5]
print(solution(A))