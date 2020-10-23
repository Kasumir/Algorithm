from sys import stdin
import sys
from collections import deque
sys.setrecursionlimit(100000)


N, M = list(map(int, stdin.readline().split()))

#graph[N][M]
graph = [[0]*M for i in range(N)]
stgraph = [[0]*M for i in range(N)]
endgrapg = [[0]*M for i in range(N)]
sumgraph = [[0]*M for i in range(N)]
for i in range(N):
    tmp = list(stdin.readline())
    for j in range(M):
        graph[i][j] = int(tmp[j])


def bfs(n, m, state, flag):
    q = deque()
    q.append([n, m])
    graph[n][m] = flag + 1
    state[n][m] = 1
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while q:
        now = q.popleft()
        for a, b in direction:
            if 0 <= now[0] + a < N and 0 <= now[1] + b < M:
                if graph[now[0] + a][now[1] + b] == flag:
                    q.append([now[0] + a, now[1] + b])
                    graph[now[0] + a][now[1] + b] = flag + 1
                    state[now[0] + a][now[1] + b] = state[now[0]][now[1]] + 1


bfs(0, 0, stgraph, 1)
bfs(N - 1, M - 1, endgrapg, 2)

ans = 99999
for n in range(N):
    for m in range(M):
        tmp = sumgraph[n][m] = stgraph[n][m] + endgrapg[n][m]
        if tmp != 0 and tmp < ans:
            ans = tmp

# for n in range(N):
#     for m in range(M):
#         print(stgraph[n][m], end=" ")
#     print()
print(ans - 1)
