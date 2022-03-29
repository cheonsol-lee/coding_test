N = int(input())
arr = list(map(int, input().split()))
max_val = max(arr)

total = 0
for score in arr:
    total += (score / max_val) * 100

print(total/N)