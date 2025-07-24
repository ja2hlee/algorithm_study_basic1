# 단지번호붙이기 : bfs버전
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True
    count = 1  # 현재 집이 포함되어서 1부터 시작

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            # 범위 내에 집이 있고 아직 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < n:
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    queue.append((nx, ny))
                    visited[ny][nx] = True
                    count += 1
    return count

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

cnt = []

for y in range(n):
    for x in range(n):
        if graph[y][x] == 1 and not visited[y][x]:
            size = bfs(x, y)
            cnt.append(size)

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])