# 33분 39초

N = int(input())
T = [0] * (N+1) # 상담일
P = [0] * (N+1) # 보수

for i in range(1, N+1):
    T_val, P_val = map(int, input().split())
    T[i] = T_val
    P[i] = P_val

dp = [0] * (N+2) # 마지막날부터 현재일까지의 최고 금액
for i in range(N, 0, -1):
    # 상담일 더했을 때, 기준일을 넘어가는 경우
    if i+T[i] > N+1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], P[i] + dp[i+T[i]])

print(dp[1])