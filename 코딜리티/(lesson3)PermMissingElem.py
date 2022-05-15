# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if len(A) == 0:
        return 1

    A.sort()
    max_val = max(A)

    for i in range(1, max_val+1):
        if i != A[i-1]:
            return i

    return max_val + 1

# A = [1,2,3,5]
A = [1]
print(solution(A))