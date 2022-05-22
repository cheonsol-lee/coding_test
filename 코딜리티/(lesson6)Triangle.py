def solution(A):
    A.sort()

    for i in range(len(A) - 2):
        if A[i] + A[i + 1] > A[i + 2]:
            return 1

    return 0

A = [10,2,5,1,8,20]
# A = [10,50,5,1]
print(solution(A))