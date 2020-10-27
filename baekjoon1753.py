from sys import stdin
from queue import PriorityQueue


V, E = list(map(int, stdin.readline().split()))
K = int(input())
graph = [[] for _ in range(V + 1)]
INF = 1e9

for _ in range(E):
    a, b, c = list(map(int, stdin.readline().split()))
    graph[a].append([b, c])


def Dijkstra(start):
    dist = [INF] * (V + 1)
    dist[start] = 0
    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        d_now, now = pq.get()

        for next, d_next in graph[now]:
            d_next += d_now
            if d_next < dist[next]:
                dist[next] = d_next
                pq.put((d_next, next))

    return dist


ans = Dijkstra(K)

for i in range(1, V + 1):
    if ans[i] != INF:
        print(ans[i])
    else:
        print("INF")

