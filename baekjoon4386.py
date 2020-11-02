from sys import stdin
from queue import PriorityQueue
import math

n = int(input())
star = []
pq = PriorityQueue()
parent = {}
rank = {}

def make_set(v):
    parent[v] = v
    rank[v] = 0

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


for i in range(n):
    a, b = map(float, stdin.readline().split())
    star.append([a, b])
    make_set(i)

for i in range(n):
    for j in range(i + 1, n):
        pq.put((math.sqrt(((star[i][0] - star[j][0]) ** 2) + ((star[i][1] - star[j][1]) ** 2)), i, j))

ans = 0
for _ in range(n):
    while not pq.empty():
        d, a, b = pq.get()
        if find(a) != find(b):
            union(a, b)
            ans += d
            break

def prim(start):
    pq = PriorityQueue()

print(round(ans, 2))


