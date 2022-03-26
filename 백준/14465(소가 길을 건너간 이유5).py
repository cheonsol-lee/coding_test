N, K, B = map(int, input().split())
arr = [0] * N

# 망가진 개수 입력
for i in range(B):
    arr[int(input())-1] = 1 # 망가진 것은 1으로 변경

start = 0
end = K
min_val = sum(arr[start:end])
cur_val = sum(arr[start:end])

# end가 끝에 도달하면 중지
while end != N:
    # 슬라이딩 윈도우내 값을 더함(망가진 신호등 개수만 구함)
    cur_val = cur_val - arr[start] + arr[end]
    min_val = min(min_val, cur_val)

    start += 1
    end += 1

print(min_val)