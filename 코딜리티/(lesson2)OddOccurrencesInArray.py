def solution(A):
    A.sort() # 정렬
    if len(A) == 1:
        return A[0]

    before = A[0]
    cnt = 1
    for val in A[1:]:
        if val == before:
            cnt += 1
            before = val
        else:
            if cnt % 2 != 0:
                return before
            before = val
            cnt = 1

    if cnt % 2 != 0:
        return before

# A = [9,3,9,3,9,7,9]
A = [1,3,3,5,5,7,7]
print(solution(A))