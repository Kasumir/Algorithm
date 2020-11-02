from sys import stdin
import sys

sys.setrecursionlimit(1000000)
N = int(stdin.readline())
M = int(stdin.readline())
graph = [[] for _ in range(N)]

for i in range(N):
    graph[i] = list(map(int, stdin.readline().split()))

plan = list(map(int, stdin.readline().split()))
parents = [i for i in range(N)]
def find(x):
    if parents[x] == x:
        return x
    else:
        p = find(parents[x])
        parents[x] = p
        return p


def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parents[y] = x

def solve():
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                union(i, j)
                graph[i][j] = 0
                graph[j][i] = 0
    p = find(plan[0] - 1)
    for i in range(1, M):
        if p != find(plan[i] - 1):
            print("NO")
            return
    print("YES")

solve()