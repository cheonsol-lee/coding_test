N, K = map(int, input().split())
arr = list(map(int, input().split()))
check_list = [0] * (N+1)
arr.append(0)

# 2를 0으로 바꿈
for i in range(N):
    if arr[i] == 2:
        arr[i] = 0

import math
start = 0
end = 0
MAX = math.pow(10, 6) + 1
min_size = MAX
sum_val = 0

while end <= N:
    if sum_val == K:
        size = end - start
        min_size = min(min_size, size)
        sum_val -= arr[start]
        start += 1

    else:
        if check_list[end] == 0:
            sum_val += arr[end]
            check_list[end] = 1
        end += 1

if min_size == MAX:
    print(-1)
else:
    print(min_size)