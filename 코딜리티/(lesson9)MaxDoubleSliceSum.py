def solution(A):
    A_len = len(A)
    left_sum = [0] * A_len
    right_sum = [0] * A_len

    for i in range(1, A_len - 1):
        left_sum[i] = max(0, left_sum[i - 1] + A[i])

    for i in range(A_len - 2, 1, -1):
        right_sum[i] = max(0, right_sum[i + 1] + A[i])

    m = 0
    for i in range(1, A_len - 1):
        m = max(m, left_sum[i - 1] + right_sum[i + 1])
    return m

A = [3,2,6,-1,4,5,-1,2]
A = [3,2,6,-1,-14,5,-1,2]
# A = [3,2,6,-1,4,5,-1,2,3,-10,5,6]
# A = [1,2,3]
# A = [-1,-2,-3]
print(solution(A))