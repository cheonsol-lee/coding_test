# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    MAX = 1000000000
    ans = 0
    cnt_1 = 0
    for i in reversed(A):
        if i == 1:
            cnt_1 += 1
        else:
            ans += cnt_1

    if ans > MAX:
        return -1
    else:
        return ans

A = [0,1,0,1,1]
print(solution(A))