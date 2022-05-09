A = []

def solution(A, K):
    if len(A) == 0:
        return []

    while K:
        last = A.pop()
        A.insert(0, last)
        K -= 1
    return A

print(solution(A, 3))