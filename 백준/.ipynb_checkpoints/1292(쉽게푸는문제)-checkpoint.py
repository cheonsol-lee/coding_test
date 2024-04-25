# 24분 27초
A, B = map(int, input().split())
sum_total = [0 for i in range(1000)]

data = []
for num in range(1, B+1):
    for _ in range(num):
        data.append(num)

print(sum(data[A-1:B]))

# 1 2 2 3 3 3 4 4 4 4 ~
# data = []
# num = 1
# while len(data) < B:
#     for _ in range(num):
#         data.append(num)
#     num += 1

# # 구간합
# sum_total[0] = 1
# for i in range(1, B):
#     sum_total[i] = sum_total[i-1] + data[i]

# sum_A = 0
# sum_B = 0
# if A == 1:
#     sum_B = sum_total[B-1]
#     sum_A = 0
# else:
#     sum_B = sum_total[B-1]
#     sum_A = sum_total[A-2]

# print(sum_B - sum_A)

