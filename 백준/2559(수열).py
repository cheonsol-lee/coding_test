N, K = map(int, input().split())
arr = list(map(int, input().split()))

max_sum = sum(arr[0:K])
cur_sum = sum(arr[0:K])
for i in range(K, N):
    cur_sum = cur_sum + arr[i] - arr[i-K]
    max_sum = max(max_sum, cur_sum)

print(max_sum)

