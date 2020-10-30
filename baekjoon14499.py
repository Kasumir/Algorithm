from sys import stdin

N, M, x, y, K = map(int, stdin.readline().split())

graph = [[] for _ in range(N)]
#graph[N][M]
for i in range(N):
    graph[i] = list(map(int, stdin.readline().split()))
command = list(map(int, stdin.readline().split()))

directions = [[0, 0], [0, 1], [0, -1], [-1, 0], [1, 0]]
dice = [0, 0, 0, 0, 0, 0, 0] #위, 동, 서, 북, 남, 아래


for com in command:
    dx, dy = directions[com]
    if 0 <= x + dx < N and 0 <= y + dy < M:
        x += dx
        y += dy
        if com == 1:
            tmp = dice[1]
            dice[1] = dice[0]
            dice[0] = dice[2]
            dice[2] = dice[6]
            dice[6] = tmp
        elif com == 2:
            tmp = dice[0]
            dice[0] = dice[1]
            dice[1] = dice[6]
            dice[6] = dice[2]
            dice[2] = tmp
            # 위, 동, 서, 북, 남, 아래
        elif com == 3:
            tmp = dice[0]
            dice[0] = dice[4]
            dice[4] = dice[6]
            dice[6] = dice[3]
            dice[3] = tmp
        elif com == 4:
            tmp = dice[0]
            dice[0] = dice[3]
            dice[3] = dice[6]
            dice[6] = dice[4]
            dice[4] = tmp

        if graph[x][y] == 0:
            graph[x][y] = dice[6]
        else:
            dice[6] = graph[x][y]
            graph[x][y] = 0
        print(dice[0])




