# 17분 49초

nm = input()
N = int(input())
team_li = []
for _ in range(N):
    team_li.append(input())

win_rate_li = [] # 우승 확률

from collections import Counter
for team_nm in team_li:
    total_nm = nm + team_nm
    counter = Counter(total_nm)
    L = counter['L']
    O = counter['O']
    V = counter['V']
    E = counter['E']

    win_rate = (((L+O)%100) * ((L+V)%100) * ((L+E)%100) * ((O+V)%100) * ((O+E)%100) * ((V+E)%100))%100
    win_rate_li.append(win_rate)

max_rate = max(win_rate_li)
max_index_li = [i for i,win_rate in enumerate(win_rate_li) if win_rate==max_rate] # 최대값이 여러개인 경우

result_li = []
for index in max_index_li:
    result_li.append(team_li[index])

result_li.sort()

print(result_li[0])
