N = int(input())

def make_binary_num(N):
    arr = list()
    while True:
        arr.append(N % 2)
        N //= 2
        if N == 0:
            break
    return arr

def count_binary_gap(arr):
    left = 0
    right = 0
    max_len = len(arr)
    cnt = 0
    max_cnt = 0
    while right < max_len and left <= right:
        if arr[left] == 1:
            if arr[right] == 0:
                cnt += 1
                right += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 0
                left = right
                right += 1

        else:
            # 둘다 0일 때
            if arr[right] == 0:
                left += 1
                right += 1
            # left만 0일때
            else:
                left = right

    return max_cnt

arr = make_binary_num(N)
# print(arr)
print(count_binary_gap(arr))


