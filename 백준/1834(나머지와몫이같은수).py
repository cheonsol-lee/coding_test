# 6분 43초
N = int(input())

val_li = []
for i in range(1, N):
    val = i * (N+1)
    val_li.append(val)

print(sum(val_li))