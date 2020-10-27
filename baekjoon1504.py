from sys import stdin
from queue import PriorityQueue

N, E = map(int, stdin.readline().split())
INF = 1000000000

graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = list(map(int, stdin.readline().split()))
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = list(map(int, stdin.readline().split()))

def Dijkstra(start):
    pq = PriorityQueue()
    dist = [INF] * (N + 1)
    pq.put((0, start))
    dist[start] = 0

    while not pq.empty():
        d_now, now = pq.get()

        for next, d_next in graph[now]:
            d_next += d_now
            if d_next < dist[next]:
                dist[next] = d_next
                pq.put((dist[next], next))


    return dist


a = Dijkstra(1)
b = Dijkstra(v1)
c = Dijkstra(v2)

ans = min(a[v1] + b[v2] + c[N], a[v2] + c[v1] + b[N])


if ans < INF:
    print(ans)
else:
    print(-1)

