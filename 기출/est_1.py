# histogram = [[0,0,0,0,0,0,1],
#              [0,0,0,1,0,0,1],
#              [0,1,0,1,0,0,1],
#              [1,1,2,2,1,0,1],
#              [2,2,2,2,1,2,2],
#              [2,2,1,1,1,2,2],
#              [2,2,1,1,1,2,2]]

# histogram = [[0,0,0,0,0],
#              [0,0,0,0,0],
#              [2,2,0,0,0],
#              [1,0,1,0,0],
#              [2,1,2,2,2],
#              [2,1,2,2,2]]

histogram = [[1,0,2],
             [1,1,2],
             [1,2,2]]



def solve(histogram):
    H = len(histogram)
    W = len(histogram[0])

    result = 1
    for j in range(0, W, 1):
        cnt = 0 # 2의 개수
        for i in range(0, H, 1):
            if histogram[i][j]==0:
                cnt = 0
            elif histogram[i][j]==1:
                break
            elif histogram[i][j]==2:
                cnt += 1
        result *= (cnt+1)
        
    return result

print(solve(histogram))