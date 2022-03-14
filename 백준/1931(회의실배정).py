N = int(input())
s,e = -1, -1
arr = []

for i in range(N):
    s, e = map(int, input().split())
    arr.append((s,e))

arr.sort()
arr = sorted(arr, key=lambda x: x[1]) # 끝나는 시간 기준으로 오름차순

e = arr[0][1]
max_count = 0
count = 1
for i in range(N-1):
    if e <= arr[i+1][0]:
        e = arr[i+1][1]
        count += 1

print(count)
