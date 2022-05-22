def solution(A):
    arr = []
    for i, val in enumerate(A):
        arr.append((i-val, -1)) # 원의 좌측점
        arr.append((i+val, 1)) # 원의 우측점

    arr.sort()

    interval = 0  # 열린 원의 수
    intersect = 0 # 겹치는 원의 수
    for i, val in enumerate(arr):
        if val[1] == 1:
            interval -= 1

        # 새 원을 열 때, 이미 열린 원의 개수를 더함(intersect)
        if val[1] == -1:
            intersect += interval
            interval += 1

    return intersect

A = [1,5,2,1,4,0]
print(solution(A))