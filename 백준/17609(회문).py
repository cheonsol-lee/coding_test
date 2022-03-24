T = int(input())
for k in range(T):
    arr = list(input())

    i = 0
    j = len(arr)-1

    # 길이가 짝수라면
    if len(arr) % 2 == 0:
        while(True):
            if arr[i] == arr[j] and i<j:
                i += 1
                j -= 1
                continue

            elif arr[i] != arr[j]:
