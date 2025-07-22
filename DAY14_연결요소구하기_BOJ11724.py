import sys #실습환경에서는 안 나는데 백준 런타임에러때문에 추가
sys.setrecursionlimit(10**6)  #런타임에러수정2:재귀 깊이 문제 방지
input = sys.stdin.readline 

def dfs(graph, v, visited):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

n, m = map(int, input().split())

# 그래프 초기화 : 노드 간 연결 정보를 저장해서 탐색하도록 
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v) # 인접행렬이 아닌 인접리스트에서는 이 방식으로 양방향 표시
    graph[v].append(u)

visited = [False] * (n + 1)

count = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1

print(count)


#BFS를 이용한 코드
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)

count = 0

for i in range(1, n + 1):
    if not visited[i]:
        bfs(graph, i, visited)
        count += 1

print(count)