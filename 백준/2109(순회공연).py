# 참조: https://velog.io/@bye9/백준파이썬-2109-순회강연
import heapq

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))

arr.sort(key=lambda x:x[1]) # 날짜 기준으로 오름차순 정렬
heap = []

for i in arr:
    heapq.heappush(heap, i[0])

    # 기준 날짜보다 힙이 클때,
    if len(heap) > i[1]:
        heapq.heappop(heap) # 맨 앞의 원소 제거(적은 강연료)

print(sum(heap))