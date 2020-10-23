from collections import deque
from sys import stdin

M, N = list(map(int, stdin.readline().split()))
graph = [[0] * M for _ in range(N)]
visit = [[False] * M for _ in range(N)]
#graph[N][M]
for i in range(N):
    tmp = list(stdin.readline())
    for j in range(M):
        graph[i][j] = int(tmp[j])


def bfs(x, y):
    q = deque()
    q.append([x, y, 0])
    visit[x][y] = True
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while q:
        now = q.popleft()
        if [now[0], now[1]] == [N - 1, M - 1]:
            return now[2]
        for a, b in directions:
            if 0 <= now[0] + a < N and 0 <= now[1] + b < M:
                if not visit[now[0] + a][now[1] + b]:
                    if graph[now[0] + a][now[1] + b] == 1:
                        q.append([now[0] + a, now[1] + b, now[2] + 1])
                        visit[now[0] + a][now[1] + b] = True
                    else:
                        q.insert(0, [now[0] + a, now[1] + b, now[2]])
                        visit[now[0] + a][now[1] + b] = True


print(bfs(0, 0))