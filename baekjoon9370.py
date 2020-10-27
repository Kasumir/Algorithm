from sys import stdin
from queue import PriorityQueue
r = stdin.readline

T = int(r())
ans = []
INF = 1000000000

def Dijkstra(start, n, graph):
    q = PriorityQueue()
    dist = [INF] * (n + 1)
    path = [[] for _ in range(n + 1)]
    dist[start] = 0
    q.put((0, start))
    path[start].append(start)

    while not q.empty():
        d_now, now = q.get()

        for next, d_next in graph[now]:
            d_next += d_now
            if d_next < dist[next]:
                dist[next] = d_next
                q.put((d_next, next))
                path[next].clear()
                for i in path[now]:
                    path[next].append(i)
                path[next].append(next)

    return dist, path

for _ in range(T):
    n, m, t = map(int, r().split()) #정점, 간선, 목적지후보
    s, g, h = map(int, r().split()) #시작점 g와 h사이 간선을 지났음
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, r().split())
        graph[a].append([b, d])
        graph[b].append([a, d])
    candidate = []
    for _ in range(t):
        candidate.append(int(r()))

    ds, ds_path = Dijkstra(s, n, graph)
    dg, _ = Dijkstra(g, n, graph)
    dh, _ = Dijkstra(h, n, graph)
    tmp = []
    for c in candidate:
        if ds[g] < ds[h]:
            if ds[g] + dg[h] + dh[c] == ds[c]:
                tmp.append(c)
        else:
            if ds[h] + dh[g] + dg[c] == ds[c]:
                tmp.append(c)
    ans.append(tmp)

for i in ans:
    i.sort()
    for j in i:
        print(j, end=" ")
    print()
