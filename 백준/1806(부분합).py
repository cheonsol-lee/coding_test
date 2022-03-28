N, S = map(int, input().split())
arr = list(map(int, input().split()))
arr.append(0)
start = 0
end = 0
MAX = 100000
min_length = MAX
part_sum = 0
while start <= end and end <= N:
    if part_sum >= S:
        min_length = min(min_length, end - start)
        part_sum -= arr[start]
        start += 1
    else:
        part_sum += arr[end]
        end += 1

if min_length == MAX:
    print(0)
else:
    print(min_length)