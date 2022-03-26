N, K = map(int, input().split())
arr = list(map(int, input().split()))
chk_list = [0] * 100001
count = 0
max_count = 0

start = 0
end = 0

while end < N:
    # K보다 적은 개수 있을 때만 count 증가
    if chk_list[arr[end]] < K:
        chk_list[arr[end]] += 1
        count += 1
        max_count = max(max_count, count)
        end += 1

    # K이상의 수가 있으면 arr[start] 값을 제거
    else:
        chk_list[arr[start]] -= 1
        start += 1
        count -= 1

print(max_count)



