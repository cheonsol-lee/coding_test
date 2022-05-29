def solution(n, times):
    times.insert(0,0)
    dp = [987654321] * (n + 1)
    dp[2] = times[1]
    if n >= 3:
        dp[3] = times[1] * 2
    if n <= 3: return dp[n]

    length = n//2 # 사용할 times 개수

    # bottom-up 동적계획법
    for j in range(4, n+1):
        for i in range(1, length+1):
            val = dp[j-i]+times[i]
            dp[j] = min(dp[j], val)

    return dp[n]

n, times = 4, [2,3]
n, times = 4, [2,30]
n, times = 3, [2,30]
n, times = 5, [2,4,5]
n, times = 6, [1,2,3]
# n, times = 7, [1,2,3,4]
print(solution(n, times))