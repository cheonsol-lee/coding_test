'''
44, 1, 0, 0, 31, 25
31, 10, 45, 1, 6, 19

0, 0, 0, 0, 0, 0
38, 19, 20, 40, 15, 25

45, 4, 35, 20, 3, 9
20, 9, 3, 45, 4, 35
'''

lottos = list(map(int, input().split(',')))
win_nums = list(map(int, input().split(',')))

rank = [6,6,5,4,3,2,1]

cnt_0 = lottos.count(0)
ans = 0
for x in win_nums:
    if x in lottos:
        ans += 1

print(rank[cnt_0 + ans], rank[ans])
