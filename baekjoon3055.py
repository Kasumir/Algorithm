from sys import stdin
from collections import deque

R, C = list(map(int, stdin.readline().split()))

graph = [['.'] * C for _ in range(R)]
visit = [[0] * C for _ in range(R)]
water = [[False] * C for _ in range(R)]
waterPoint = []

for i in range(R):
    tmp = list(stdin.readline())
    for j in range(C):
        graph[i][j] = tmp[j]
        if tmp[j] == '*':
            waterPoint.append([i, j])
        if tmp[j] == 'D':
            end = [i, j]
        if tmp[j] == 'S':
            start = [i, j]


direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def explode():
    q = []
    for wp in waterPoint:
        q.append(wp)
        water[wp[0]][wp[1]] = True

    while q:
        now = q.pop()
        for a, b in direction:
            x = now[0] + a
            y = now[1] + b
            if 0 <= x < R and 0 <= y < C:
                if not water[x][y] and graph[x][y] == '.':
                    waterPoint.append([x, y])
                    water[x][y] = True

    # for i in range(R):
    #     for j in range(C):
    #         if water[i][j]:
    #             print('*', end=" ")
    #         else:
    #             print(graph[i][j], end=" ")
    #     print()

def bfs(x, y):
    q = deque()
    q.append([x, y, 0])
    visit[x][y] = 1
    time = 0
    while q:
        now = q.popleft()
        if [now[0], now[1]] == end:
            return now[2]

        if time == now[2]:
            time += 1
            explode()
        for a, b in direction:
            x = now[0] + a
            y = now[1] + b
            if 0 <= x < R and 0 <= y < C:
                if visit[x][y] == 0 and not water[x][y] and graph[x][y] != 'X':
                    visit[x][y] = 1
                    q.append([x, y, now[2] + 1])

ans = bfs(start[0], start[1])
if ans:
    print(ans)
else:
    print("KAKTUS")