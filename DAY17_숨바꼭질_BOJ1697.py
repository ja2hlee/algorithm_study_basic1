from collections import deque

def bfs(n, k):
    MAX = 100001
    visited = [False] * MAX
    time = [0] * MAX  #각 위치에 도달하는 데 걸린 시간

    queue = deque()
    queue.append(n)
    visited[n] = True

    while queue:
        current = queue.popleft()

        if current == k:
            return time[current]  #동생에게 도달한 가장 빠른 시간 반환

        for next_pos in [current - 1, current + 1, current * 2]:
            if 0 <= next_pos < MAX and not visited[next_pos]:
                visited[next_pos] = True #방문한 곳을 True로 바꿔서 방문X
                time[next_pos] = time[current] + 1
                queue.append(next_pos)

# 입력 받기
n, k = map(int, input().split())
print(bfs(n, k))



