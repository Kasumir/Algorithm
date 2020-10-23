from sys import stdin
from collections import deque

MAX = 100000
MIN = 0
visit = [0] * (MAX + 1)
N, K = list(map(int, stdin.readline().split()))

def bfs(start):
    q = deque()
    q.append([start, 0])
    visit[start] = 1
    while q:
        now = q.popleft()
        if now[0] == K:
            return now[1]
        if MIN <= now[0] - 1 <= MAX and visit[now[0] - 1] == 0:
            q.append([now[0] - 1, now[1] + 1])
            visit[now[0] - 1] = 1
        if MIN <= now[0] + 1 <= MAX and visit[now[0] + 1] == 0:
            q.append([now[0] + 1, now[1] + 1])
            visit[now[0] + 1] = 1
        if MIN <= now[0] * 2 <= MAX and visit[now[0] * 2] == 0:
            q.append([now[0] * 2, now[1] + 1])
            visit[now[0] * 2] = 1


print(bfs(N))