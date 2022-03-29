N, M = map(int, input().split())

arr1 = []
arr2 = []
prefix_arr2 = [0] * 10000 # arr2가 접두사로써 최소 1번 이상 사용되면 1, 아니면 0

for i in range(N):
    arr1.append(input())

for i in range(M):
    arr2.append(input())

for i in range(N):
    for j in range(M):
        # 이미 접두사로 확인된 단어는 패스
        if prefix_arr2[j] == 1:
            continue

        # 앞글자가 다르면 패스
        if arr2[j][0] != arr1[i][0]:
            continue

        length = len(arr2[j])
        # if arr1[i][:length] == arr2[j]:
        #     prefix_arr2[j] = 1

        if arr1[i].startswith(arr2[j]):
            prefix_arr2[j] = 1

print(sum(prefix_arr2))