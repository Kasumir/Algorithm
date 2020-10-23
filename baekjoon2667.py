from sys import stdin
import sys
sys.setrecursionlimit(1000000)

N = int(stdin.readline())
graph = [[0] * N for _ in range(N)]
for i in range(N):
    tmp = list(stdin.readline())
    for j in range(N):
        graph[i][j] = int(tmp[j])


U = [0, 1]
D = [0, -1]
L = [-1, 0]
R = [1, 0]
direction = [U, D, L, R]

def dfs(x, y, z):
    graph[x][y] = z
    global count
    count += 1
    for a, b in direction:
        if 0 <= x + a < N and 0 <= y + b < N:
            if graph[x + a][y + b] == 1:
                dfs(x + a, y + b, z)


color = 2
ans = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count = 0
            dfs(i, j, color)
            ans.append(count)
            color += 1

print(color - 2)
ans.sort()
for i in ans:
    print(i)