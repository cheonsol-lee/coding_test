import math
D, H, W = map(int, input().split())
k = math.sqrt((D**2)/(H**2 + W**2))
h = int(k * H)
w = int(k * W)
print(h, w)