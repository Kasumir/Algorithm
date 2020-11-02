from sys import stdin

n, m = map(int, stdin.readline().split())

parent = [i for i in range(n + 1)]

def find(x):
    if x == parent[x]:
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

ans = []
for _ in range(m):
    com, a, b = map(int, stdin.readline().split())
    if com == 0:
        union(a, b)
    elif com == 1:
        if find(a) == find(b):
            ans.append("YES")
        else:
            ans.append("NO")

for i in ans:
    print(i)


