N = int(input())
arr = list(map(int, input().split()))
arr.sort() #오름차순

start = 0
end = N - 1
min_val = 2000000001
ans_l = arr[0]
ans_r = arr[N - 1]

while start < end:
    ans = arr[start] + arr[end]
    if min_val > abs(ans):
        min_val = abs(ans)
        ans_l = arr[start]
        ans_r = arr[end]

    if ans > 0:
        end -= 1

    else:
        start += 1

print(ans_l, ans_r)