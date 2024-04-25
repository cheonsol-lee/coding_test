# 4분 32초
X, Y = input().split()
X_r = int(X[::-1])
Y_r = int(Y[::-1])

total = str(X_r+Y_r)
total = total[::-1]
print(int(total))