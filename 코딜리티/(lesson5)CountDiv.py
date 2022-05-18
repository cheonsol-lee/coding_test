def solution(A, B, K):
    init = 0
    for i in range(A, B+1):
        if i % K == 0:
            init = i # 처음으로 나누어지는 수
            break

    if A == B:
        return 1 if A%K == 0 else 0
    return B//K - init//K + 1

A = 10
B = 10
K = 4
print(solution(A, B, K))