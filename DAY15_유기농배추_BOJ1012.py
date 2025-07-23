import sys
sys.setrecursionlimit(10**6)
#input = sys.stdin.readline

# 상하좌우 이동을  위한 추가
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    #(x,y)의 연결 위치의 배추를 방문하기 위함
    visited[y][x] = True #현재 방문 위치
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < m and 0 <= ny < n:
            if field[ny][nx] == 1 and not visited[ny][nx]:
                dfs(nx, ny)

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    field = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1 #배추좌표 1로 바꾸기
    
    count = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1 and not visited[i][j]:
                dfs(j, i)
                count += 1
    print(count)


