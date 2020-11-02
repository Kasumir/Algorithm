from sys import stdin
from queue import PriorityQueue
import math

N, M = map(int, stdin.readline().split())
gods = [[0, 0]]
parent = {}

def make_set(v):
    parent[v] = v

def find(x):
    if parent[x] == x:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return p

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x

for i in range(1, N + 1):
    a, b = map(int, stdin.readline().split())
    gods.append([a, b])
    make_set(i)


for _ in range(M):
    a, b = map(int, stdin.readline().split())
    union(a, b)

pq = PriorityQueue()
for i in range(1, N):
    for j in range(i + 1, N + 1):
        dis = math.sqrt(((gods[i][0] - gods[j][0]) ** 2) + ((gods[i][1] - gods[j][1]) ** 2))
        pq.put((dis, i, j))

ans = 0

while not pq.empty():
    d, x, y = pq.get()
    if find(x) != find(y):
        union(x, y)
        ans += d

print(format(ans,".2f"))



