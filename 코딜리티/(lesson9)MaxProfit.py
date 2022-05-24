def solution(A):
    # 값이 비어있으면 0 리턴
    if not A:
        return 0

    min_val = A[0]
    max_profit = 0

    for i in range(1, len(A)):
        if min_val > A[i]:
            min_val = A[i]
        else:
            profit = A[i] - min_val
            max_profit = max(max_profit, profit)

    return max_profit

A = [23171,21011,21123,21366,21013,21367]
print(solution(A))