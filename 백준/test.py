# # 1번 : 물약 구매
# N = int(input())
# check_arr = [0] * N
# price_arr = list(map(int, input().split()))
# discount_arr = []
# for i in range(N):
#     count = int(input())
#     tmp_arr = []
#     for j in range(count):
#         num, price = map(int, input().split())
#         tmp_arr.append((num-1,price))
#
#     discount_arr.append(tmp_arr)
#
# # print(discount_arr)
# # print(len(discount_arr[0]))
# MAX = 1001
# total = 0
#
# for i in range(N):
#     min_price = min(price_arr)
#     index = price_arr.index(min_price)
#
#     # 최소값이 여러개라면
#     if price_arr.count(min_price) != 1:
#         max_val = 0
#         result_list = [i for i, value in enumerate(price_arr) if value == min_price]  # [1 ,3]
#         for j in result_list:
#             if len(discount_arr[j]) == 0:
#                 continue
#             if max_val < len(discount_arr[j]):
#                 max_val = max(max_val, len(discount_arr[j]))
#                 index = j
#
#     total += price_arr[index]
#
#     price_arr[index] = MAX
#     check_arr[index] = 1
#
#     # 할인 가격 반영
#     for discount in discount_arr[index]:
#         price = price_arr[discount[0]] - discount[1]
#         # 이미 구매했으면 할인하지 않고 넘어감
#         if check_arr[discount[0]] == 1:
#             continue
#
#         if price <= 0:
#             price_arr[discount[0]] = 1
#         else:
#             price_arr[discount[0]] = price
#
# print(total)

# 2번

# # 최소값이 여러개라면
# if price_arr.count(min_price) != 1:
#     # enumerate
#     result_list = [i for i, value in enumerate(price_arr) if value == min_price]  # [1 ,3]

# 3번

# print(len(list(itertools.combinations(range(1, 4), 2))))
# # 조합
# def comb(n, r):
#     val1 = 1
#     val2 = 1
#     val3 = 1
#     # n!
#     for i in range(1,n+1):
#         val1 *= i
#
#     # (n-r)!
#     for i in range(1,(n-r)+1):
#         val2 *= i
#
#     # r!
#     for i in range(1,r+1):
#         val3 *= i
#
#     return int(val1 / (val2*val3))
#
# import itertools
# N = int(input())
# b_arr = input()
# arr = []
# for word in b_arr:
#     if word == 'W' or word == 'H' or word == 'E':
#         arr.append(word)
#
# N = len(arr)
# count = 0
# MOD = 1000000007
# memo = [[0]*N for i in range(N)]
#
# for i in range(N):
#     if arr[i] != 'W':
#         continue
#
#     for j in range(i, N):
#         if arr[j] != 'H':
#             continue
#         n = arr[j+1:].count('E')
#         for r in range(2, n+1):
#             if memo[n][r] != 0:
#                 count += memo[n][r]
#             else:
#                 memo[n][r] = len(list(itertools.combinations(range(1, n+1), r))) % MOD
#                 # memo[n][r] = (comb(n, r)%MOD)
#                 count = (count + memo[n][r]) % MOD
#
# print(count % MOD)
