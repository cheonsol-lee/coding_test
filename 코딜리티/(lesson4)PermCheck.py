# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if len(A) == 1 and A[0] != 1:
        return 0

    A.sort()
    before = A[0]
    for val in A[1:]:
        if before+1 == val:
            before = val
        else:
            return 0

    if max(A) == len(A):
        return 1
    else:
        return 0


A = [4]
print(solution(A))
