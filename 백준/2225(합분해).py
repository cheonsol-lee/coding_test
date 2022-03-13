N, K = map(int, input().split())

dp = [[0] * 201 for i in range(201)]
dp[0] = [1] * 201
MOD = 1000000000

for i in range(1, N+1):
    for j in range(1, K+1):
        for col in range(1, j+1):
            dp[i][j] += (dp[i-1][col])%MOD

print(dp[N][K]%MOD)