N, M = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
i = 0
j = 1
while i <= j and j < N:
    diff = sum(arr[i:j])

    if diff == M:
        count += 1
        i += 1
        j += 1
        continue

    elif diff < M:
        j += 1
        continue

    elif diff > M:
        i += 1
        continue

print(count)




