from sys import stdin
import sys

sys.setrecursionlimit(1000000)

def dfs(now, color):
    global visit
    global graph
    visit[now] = color
    for i in graph[now]:
        if visit[i] == 0:
            dfs(i, -color)


K = int(stdin.readline())
ans = []
for _ in range(K):
    V, E = list(map(int, stdin.readline().split()))
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = list(map(int, stdin.readline().split()))
        graph[a].append(b)
        graph[b].append(a)
    visit = [0] * (V + 1)
    for i in range(1, V + 1):
        if visit[i] == 0:
            dfs(i, 1)

    tmp = True
    for i in range(1, V + 1):
        for j in graph[i]:
            if visit[i] == visit[j]:
                tmp = False

    if tmp:
        ans.append("YES")
    else:
        ans.append("NO")

for i in ans:
    print(i)