from collections import deque

N, K = map(int, input().split())
MAX = 100001
visit = [0] * MAX

def bfs(start):
    q = deque()
    q.append([start, 0])
    visit[start] = 1
    while q:
        now = q.popleft()
        if now[0] * 2 < MAX and visit[now[0] * 2] == 0:
            q.insert(0, [now[0] * 2, now[1]])
            visit[now[0] * 2] = 1


        if now[0] == K:
            return now[1]

        if now[0] + 1 < MAX and visit[now[0] + 1] == 0:
            q.append([now[0] + 1, now[1] + 1])
            visit[now[0] + 1] = 1

        if now[0] - 1 >= 0 and visit[now[0] - 1] == 0:
            q.append([now[0] - 1, now[1] + 1])
            visit[now[0] - 1] = 1


print(bfs(N))