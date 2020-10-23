from collections import deque

S = int(input())
MAX = 1001
graph = [[0] * MAX for _ in range(MAX)]

def bfs(start):
    q= deque()
    q.append([start, 0, 0])
    graph[start][0] = 1
    while q:
        now = q.popleft()
        if now[0] == S:
            return now[2]

        if graph[now[0]][now[0]] == 0:
            q.append([now[0], now[0], now[2] + 1])
            graph[now[0]][now[0]] = 1
        if now[1] != 0 and now[0] + now[1] < MAX and graph[now[0] + now[1]][now[1]] == 0:
            q.append([now[0] + now[1], now[1], now[2] + 1])
            graph[now[0] + now[1]][now[1]] = 1
        if now[0] - 1 >= 0 and graph[now[0] - 1][now[1]] == 0:
            q.append([now[0] - 1, now[1], now[2] + 1])
            graph[now[0] - 1][now[1]] = 1

print(bfs(1))
