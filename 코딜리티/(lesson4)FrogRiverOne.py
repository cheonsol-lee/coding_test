# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    arr = [0] * 100001
    cnt = 0
    index = -1
    for i, val in enumerate(A):
        if arr[val] == 0:
            arr[val] = 1

            if val <= X:
                cnt += 1
                index = i

        if cnt == X:
            return i

    return -1

X = 5
# A = [1,3,1,4,2,3,5,4]
A = [1,3,1,4,2,3,4,4]
print(solution(X, A))