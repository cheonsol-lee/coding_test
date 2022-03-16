import copy

N = int(input())
arr1 = list(map(int, input()))
arr2 = list(map(int, input()))
arr_copy1 = copy.deepcopy(arr1)
arr_copy2 = copy.deepcopy(arr1)
count = 0

def push_button(arr1 ,arr2 , N):
    count = 0  # 스위치 누른 횟수

    for i in range(1, N):
        if arr1[i - 1] == arr2[i - 1]:
            continue
        else:
            arr1[i - 1] = 1 - arr1[i - 1]
            arr1[i] = 1 - arr1[i]

            # 맨 끝항 아닐때
            if i != N - 1:
                arr1[i + 1] = 1 - arr1[i + 1]

            count += 1

    # 답을 찾을경우
    if arr1 == arr2:
        return count
    else:
        return -1


# 0번 스위치 누르기 X
count = push_button(arr_copy1, arr2, N)
if count != -1:
    print(count)

# 0번 스위치 누르기 O
else:
    arr_copy2[0] = 1 - arr_copy2[0]
    arr_copy2[1] = 1 - arr_copy2[1]

    count = push_button(arr_copy2, arr2, N)
    if count != -1:
        print(count + 1) # 0번을 미리 눌렀으므로 1더함
    else:
        print(-1)

