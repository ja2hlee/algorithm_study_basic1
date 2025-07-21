from collections import deque

# DFS 함수 정의 (재귀)
def dfs(graph, v, visited):
    visited[v] = True #방문 처리
    print(v, end=' ') #방문한 노드를 출력
    
    for neighbor in range(1, len(graph)): #현재 노드와 연결된 이웃노드를 확인
        if graph[v][neighbor] == 1 and not visited[neighbor]: #이웃노드에 아직 방문하지 않았다면
            dfs(graph, neighbor, visited) #재귀 호출 (더 깊이 들어감)

# BFS 함수 정의 (큐)
def bfs(graph, start, visited):
    queue = deque([start]) #시작 노드를 큐에 넣음
    visited[start] = True #방문 처리
    
    while queue:
        v = queue.popleft() #하나씩 큐에서 꺼냄 (제일 앞을 꺼내는 것)
        print(v, end=' ') #방문 노드 출력
        
        for neighbor in range(1, len(graph)): #이웃노드 확인해서
            if graph[v][neighbor] == 1 and not visited[neighbor]: #안 가본 곳은
                visited[neighbor] = True
                queue.append(neighbor) #큐에 추가 (나중에 방문)

                
n,m,v = map(int,input().split())

#행렬 만들기
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range (m):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

#방문 리스트 행렬
visited_dfs = [False] * (n + 1)
visited_bfs = visited_dfs.copy()


dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)




