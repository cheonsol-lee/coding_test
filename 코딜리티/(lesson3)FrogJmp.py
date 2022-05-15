# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    num = Y - X
    cnt = num // D
    if num % D != 0:
        cnt += 1
    return cnt

X = 10
Y = 85
D = 30
print(solution(X, Y, D))
