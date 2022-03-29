T = list(input())
P = list(input())

len_T = len(T)
len_P = len(P)

arr_loc = []
cnt = 0
for i in range(len_T - len_P):
    if T[i:i+len_P] == P:
        arr_loc.append(i+1)
        cnt += 1

print(cnt)
print(' '.join(map(str, arr_loc)))

# 1번 인덱스부터 사용하므로 0번 인덱스는 '0'으로 채우고 사용안함
# T.insert(0, '0')
# P.insert(0, '0')

# # 원소 별로 최대 k값 계산
# def calculate_k(arr):
#     arr_k = [0] * (len(arr) + 1)
#
#     # 뒤에서부터 하나씩 비교
#     for j in range(len(arr), 0, -1):
#         # j의 짝수 여부에 따라 다름
#         if (j % 2 == 0):
#             k = j // 2 - 1
#         else:
#             k = j // 2
#
#         # 큰 수부터 줄여나가면서 최대 k 값 찾음
#         while k <= (j-k):
#             if arr[1:k+1] == arr[j-k:j]:
#                 break
#             else:
#                 k -= 1
#                 continue
#
#         # j번째 값에 해당하는 최대 k
#         arr_k[j] = k
#
#     return arr_k
#
# arr_k = calculate_k(P)
# print(arr_k)