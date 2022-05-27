def solution(N):
    i = 1
    cnt = 0
    while i**2 <= N:
        if i ** 2 == N:
           cnt += 1
        elif N % i == 0:
            cnt += 2
        i += 1

    return cnt

print(solution(2))