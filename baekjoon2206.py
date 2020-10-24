from collections import deque
from sys import stdin

N, M = list(map(int, stdin.readline().split()))
graph = [[0] * M for _ in range(N)]
visit = [[[0] * 2 for _ in range(M)] for _ in range(N)]
#graph[n][m]

for i in range(N):
    tmp = list(stdin.readline())
    for j in range(M):
        graph[i][j] = int(tmp[j])


def bfs(n, m):
    q = deque()
    q.append([n, m, 1, 0])
    visit[n][m][0] = 1
    visit[n][m][1] = 1
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    while q:
        a, b, d, c = q.popleft()
        #print(a, b)
        if [a, b] == [N - 1, M - 1]:
            return d

        for x, y in directions:
            if 0 <= a + x < N and 0 <= b + y < M:
                if graph[a + x][b + y] == 1 and c == 0:
                    visit[a + x][b + y][0] = visit[a + x][b + y][1] = 1
                    q.append([a + x, b + y, d + 1, 1])
                elif graph[a + x][b + y] == 0 and visit[a + x][b + y][c] == 0:
                    visit[a + x][b + y][c] = 1
                    q.append([a + x, b + y, d + 1, c])


ans = bfs(0, 0)
if ans is not None:
    print(ans)
else:
    print(-1)


