N = int(input())
stu_map = []
for i in range(N):
    stu_map.append(list(map(int, input().split())))

adj_li = [[0 for i in range(N)] for j in range(N)] #행,열은 학생번호, 같은 반 된적있으면 1

for grade in range(5):
    for i in range(N):
        for j in range(i+1, N):
            if stu_map[i][grade] == stu_map[j][grade]:
                adj_li[i][j] = 1
                adj_li[j][i] = 1

stu_cnt = [] # 학생별 같은반 된 적이 있는 횟수
for i in range(N):
    stu_cnt.append(adj_li[i].count(1)) 

print(stu_cnt.index(max(stu_cnt)) + 1) 