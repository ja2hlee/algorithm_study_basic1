from collections import deque

def bfs(n, k):
    MAX = 100001
    visited = [False] * MAX
    time = [0] * MAX #각 위치에 도달하는 데 걸린 시간
    count = [0] * MAX #각 위치에 도달하는 방법의 수

    queue = deque()
    queue.append(n)
    visited[n] = True
    count[n] = 1 #수빈이가 이미 자신의 위치에 도달해서 1임

    while queue:
        current = queue.popleft()

        for next_pos in [current - 1, current + 1, current * 2]:
            if 0 <= next_pos < MAX:
                if not visited[next_pos]:
                    visited[next_pos] = True
                    time[next_pos] = time[current] + 1 
                    count[next_pos] = count[current] 
                    #next_pos도달위치 & current지금위치->current에서 next_pos로 가기 우함
                    queue.append(next_pos)
                #같은최소시간있으먼 누적
                elif time[next_pos] == time[current] + 1:
                    count[next_pos] += count[current]#경로 누적합

    return time[k], count[k]

n, k = map(int, input().split())
shortest_time, num_ways = bfs(n, k)
print(shortest_time)
print(num_ways)
