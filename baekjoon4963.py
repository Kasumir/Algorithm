from sys import stdin
import sys
sys.setrecursionlimit(1000000)

def dfs(x, y):
    global graph
    global w, h

    graph[x][y] = 0

    u = [0, 1]
    d = [0, -1]
    l = [-1, 0]
    r = [1, 0]
    ul = [-1, 1]
    ur = [1, 1]
    dl = [-1, -1]
    dr = [1, -1]
    direction = [u, d, l, r, ul, ur, dl, dr]
    for a, b in direction:
        if 0 <= x + a < h and 0 <= y + b < w:
            if graph[x + a][y + b] == 1:
                dfs(x + a, y + b)

ans = []
while True:
    w, h = list(map(int, stdin.readline().split()))
    if w == 0 and h == 0:
        break

    graph = [[] for _ in range(h)]
    for i in range(h):
        graph[i] = list(map(int, stdin.readline().split()))

    count = 0
    for i in range(w):
        for j in range(h):
            if graph[j][i] == 1:
                dfs(j, i)
                count += 1
    ans.append(count)

for i in ans:
    print(i)