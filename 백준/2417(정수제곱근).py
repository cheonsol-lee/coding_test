n = int(input())

def binary_search(target, start, end):
    result = -1
    while start <= end:
        mid = (start + end) // 2
        num = mid ** 2
        if num >= target:
            result = mid
            end = mid - 1
        else:
            start = mid + 1

    return result

start = 0
end = n
print(binary_search(n, start, end))