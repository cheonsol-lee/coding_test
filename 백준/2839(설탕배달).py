# 23분
# # 그리디
# N = int(input())
# cnt = 0
# while True:
#     if N % 5 != 0:
#         N -= 3
#         cnt += 1
#     elif N % 5 == 0:
#         cnt += N // 5
#         print(cnt)
#         break

#     if N < 0:
#         print(-1)
#         break

# DP
N = int(input())
dp = [-1] * 5001
dp[3] = 1
dp[5] = 1

for i in range(6, N+1):
    if i % 5 == 0:
        dp[i] = dp[i-5] + 1
    elif i % 3 == 0:
        dp[i] = dp[i-3] + 1
    elif dp[i-3] > 0 and dp[i-5] > 0:
            dp[i] = min(dp[i-3], dp[i-5]) + 1

print(dp[N])