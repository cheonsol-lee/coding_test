# 1시간15초
N = int(input())
A = list(map(int, input().split()))
stack = []
NGE_li = [-1] * N
for i in range(N):
    while stack and A[stack[-1]]<A[i]:
        NGE_li[stack[-1]] = A[i]
        stack.pop()
    
    stack.append(i)
    
for i in range(N):
    print(NGE_li[i], end=' ')