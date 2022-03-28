N = int(input())
arr = list(map(int, input().split()))
K = int(input())

arr.sort()

start = 0
end = N-1
count = 0
total_sum = 0
while start < end:
    total_sum = arr[start] + arr[end]
    if total_sum == K:
        count += 1
        start += 1
        end -= 1
    elif total_sum > K:
        end -= 1
    else:
        start += 1

print(count)