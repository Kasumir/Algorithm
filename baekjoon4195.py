from sys import stdin
import sys

sys.setrecursionlimit(1000000)
T = int(stdin.readline())
parents = []


def find(x):
    if parents[x][0] == x:
        return parents[x]
    else:
        p = find(parents[x][0])
        parents[x] = p
        return p


def union(x, y):
    x, num_x = find(x)
    y, num_y = find(y)
    if x != y:
        parents[y][0] = x
        parents[y][1] = num_x + num_y
        parents[x][1] = num_x + num_y
        return num_x + num_y
    else:
        return num_x

ans = []
for _ in range(T):
    F = int(stdin.readline())
    parents = []
    idx = 0
    rel = dict()
    for i in range(F):
        a, b = map(str, stdin.readline().split())
        if a not in rel.keys():
            rel[a] = idx
            parents.append([idx, 1])
            idx += 1
        if b not in rel.keys():
            rel[b] = idx
            parents.append([idx, 1])
            idx += 1
        ans.append(union(rel[a], rel[b]))


for i in ans:
    print(i)


