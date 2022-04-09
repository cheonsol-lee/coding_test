N, gr, gc = map(int, input().split())
num = 0

# 4구간 중 어느 곳에 위치한지 파악한 후에 구간 번호에 맞게 끔 num을 채움
def solve(r, c, size):
    global num, gr, gc

    nsize = int(size / 2)
    position = nsize ** 2

    # 1구간
    if r + 0 <= gr < r + nsize and c + 0 <= gc < c + nsize:
        num += position * 0
        nr = r + nsize * 0
        nc = c + nsize * 0

    # 2구간
    elif r + 0 <= gr < r + nsize and c + nsize <= gc < c + size:
        num += position * 1
        nr = r + nsize * 0
        nc = c + nsize * 1

    # 3구간
    elif r + nsize <= gr < r + size and c + 0 <= gc < c + nsize:
        num += position * 2
        nr = r + nsize * 1
        nc = c + nsize * 0

    # 4구간
    elif r + nsize <= gr < r + size and c + nsize <= gc < c + size:
        num += position * 3
        nr = r + nsize * 1
        nc = c + nsize * 1

    if nsize == 1:
        print(num)
        return
    else:
        solve(nr, nc, nsize)


solve(0, 0, 2**N)