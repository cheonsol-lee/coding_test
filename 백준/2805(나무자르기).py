N, M = map(int, input().split())
arr = list(map(int, input().split()))

def binary_search(arr, target, start, end):
    height = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0 # 가져갈 나무 길이

        for i in arr:
            if i > mid:
                total += i - mid # 잘린 길이 합침

        if total < target:
            end = mid - 1
        else:
            # 적어도 target 이상의 길이는 가져가는 높이 저장
            height = mid
            start = mid + 1

    return height

start = 0
end = max(arr)
print(binary_search(arr, M, 0, end))

