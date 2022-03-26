<<<<<<< Updated upstream
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
=======
import copy

T = int(input())

for i in range(T):
    arr1 = list(input())
    token = False
    arr2 = copy.deepcopy(arr1)
    arr2.reverse() # 뒤집은 문자열리스트 저장

    if arr1 == arr2:
        print(0)

    else:
        length = len(arr1)
        # 뒤집어서 비교하므로 절반까지만 비교함
        for j in range(length//2 + 1):
            if arr1[j] == arr2[j]:
                continue

            # 다른 값이 나오면 그 값을 제거
            elif arr1[j] == arr2[j+1] and token == False:
                arr2.pop(j) # j 인덱스의 값 제거
                arr1.pop(length - j - 1)
                token = True
            elif arr1[j+1] == arr2[j] and token == False:
                arr1.pop(j)
                arr2.pop(length - j - 1)
                token = True
            else:
                token = False
                break

        if token == True:
            print(1)
        else:
            print(2)
>>>>>>> Stashed changes
