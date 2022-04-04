T = int(input())

for i in range(T):
    A, n = map(int, input().split())
    arr = []
    while True:
        arr.append(A % n)
        A //= n

        if A == 0: break

    if arr[:] == arr[::-1]:
        print(1)
    else:
        print(0)