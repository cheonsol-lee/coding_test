N = int(input())
arr = list(map(int, input().split()))

arr.sort()
total_sum = 0
for i in range(N):
    total_sum += sum(arr[0:i+1])

print(total_sum)
