N, K = map(int, input().split())
coin = []
count = [0] * N
for i in range(N):
    coin.append(int(input()))

for i in range(N-1, -1, -1):
    count[i] = K // coin[i]
    K %= coin[i]

print(sum(count))