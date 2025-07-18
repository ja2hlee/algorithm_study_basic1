from itertools import combinations

n = int(input())
ability = [list(map(int, input().split())) for _ in range(n)]
min_gap = float('inf') #무한대로 그냥 큰 수 비교용

players = [i for i in range(n)]
combi = list(combinations(players, n // 2))  

for i in range(len(combi) // 2):
    start_team = combi[i]
    link_team = [p for p in players if p not in start_team]

    start_ability = 0
    link_ability = 0
    for a, b in combinations(start_team, 2):
        start_ability += ability[a][b] + ability[b][a]
    for a, b in combinations(link_team, 2):
        link_ability += ability[a][b] + ability[b][a]

    gap = abs(start_ability - link_ability)
    min_gap = min(min_gap, gap)

print(min_gap)