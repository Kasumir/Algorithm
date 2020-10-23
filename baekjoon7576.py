from sys import stdin
from collections import deque

M, N = list(map(int, stdin.readline().split()))
#graph[N][M]
graph = []

for i in range(N):
    graph.append(list(map(int, stdin.readline().split())))

cnt = 0
points = []
for m in range(M):
    for n in range(N):
        if graph[n][m] == 0:
            cnt += 1
        elif graph[n][m] == 1:
            points.append([n, m])

def bfs(starts):
    q = deque()
    for a, b in starts:
        q.append([a, b, 1])
        graph[a][b] = 1

    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while q:
        now = q.popleft()
        for x, y in directions:
            if 0 <= now[0] + x < N and 0 <= now[1] + y < M:
                if graph[now[0] + x][now[1] + y] == 0:
                    q.append([now[0] + x, now[1] + y, now[2] + 1])
                    graph[now[0] + x][now[1] + y] = now[2] + 1


if cnt == 0:
    print(0)
else:
    bfs(points)

    cnt = 0
    ans = 0
    for m in range(M):
        for n in range(N):
            if graph[n][m] == 0:
                cnt += 1
            else:
                if graph[n][m] > ans:
                    ans = graph[n][m]

    if cnt:
        print(-1)
    else:
        print(ans - 1)



