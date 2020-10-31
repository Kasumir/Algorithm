from sys import stdin

N, M = map(int, stdin.readline().split())
#북0 동1 남2 서3
r, c, d = map(int, stdin.readline().split())

graph = [[] for _ in range(N)]
visited = [[False] * M for _ in range(N)]
#grapg N M
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
for i in range(N):
    graph[i] = list(map(int, stdin.readline().split()))
ans = 1

visited[r][c] = True
while True:
    dir_ok = False
    for i in range(1, 5):
        tmp_d = (d - i) % 4
        tmp_r, tmp_c = [r + directions[tmp_d][0], c + directions[tmp_d][1]]
        if graph[tmp_r][tmp_c] == 0 and not visited[tmp_r][tmp_c]:
            r = tmp_r
            c = tmp_c
            d = tmp_d
            dir_ok = True
            visited[r][c] = True
            ans += 1
            break
    if not dir_ok:
        tmp_d = (d - 2) % 4
        tmp_r, tmp_c = [r + directions[tmp_d][0], c + directions[tmp_d][1]]
        if graph[tmp_r][tmp_c] != 1:
            r = tmp_r
            c = tmp_c
        else:
            break

print(ans)

