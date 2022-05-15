# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    dp = [0] * 100001
    dp[0] = A[0]

    for i in range(1, len(A)):
        dp[i] = dp[i-1] + A[i]

    max_sum = dp[len(A)-1]
    min_val = 987654321

    for P in range(0, len(A)-1):
        diff = abs(2*dp[P] - max_sum)
        min_val = min(min_val, diff)

    return min_val


A = [3,1,2,4,3]
print(solution(A))