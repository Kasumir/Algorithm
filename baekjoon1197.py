from sys import stdin
from queue import PriorityQueue
import sys

V, E = map(int, stdin.readline().split())
inf = sys.maxsize

graph = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

def Dijkstra(start):
    pq = PriorityQueue()
    pq.put((0, start))
    dist = [inf] * (V + 1)
    dist[start] = 0
    while not pq.empty():
        now_d, now_p = pq.get()
        for next_p, next_d in graph[now_p]:
            next_d += now_d
            if next_d < dist[next_p]:
                dist[next_p] = next_d
                pq.put([next_d, next_p])

def kruskal(start):
    pq = PriorityQueue()
    for i in range(len(graph[start])):
        next_p, next_d = graph[start].pop()
        graph[next_p].pop(graph[next_p].index([start, next_d]))
        pq.put([next_d, start, next_p])

    visited = [False] * (V + 1)
    visited[start] = True
    ans = 0
    for _ in range(V):
        while not pq.empty():
            d, x, y = pq.get()
            for p in [x, y]:
                if not visited[p]:
                    for i in range(len(graph[p])):
                        next_p, next_d = graph[p].pop()
                        graph[next_p].pop(graph[next_p].index([p, next_d]))
                        pq.put([next_d, p, next_p])
                    visited[p] = True
                    ans += d
                    break
    return ans

print(kruskal(1))
