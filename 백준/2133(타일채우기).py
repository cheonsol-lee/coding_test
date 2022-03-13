# 그림 참조: https://blog.naver.com/zdudmanz/222285104463
N = int(input())

dp = [0] * 31
dp[2] = 3

# 홀수
if N % 2 != 0:
    print(0)
else:
    for i in range(4, N+1, 2):
        dp[i] = dp[i - 2] * 3 + 2

        for j in range(0, i - 2, 2):
            dp[i] += dp[i - (4 + j)] * 2

    print(dp[N])

