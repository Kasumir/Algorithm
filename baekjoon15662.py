from sys import stdin

T = int(stdin.readline())
gear = [[] for _ in range(T + 1)]

for i in range(1, T + 1):
    s = list(stdin.readline())
    tmp = []
    for j in range(8):
        tmp.append(int(s[j]))
    gear[i] = tmp

K = int(stdin.readline())
rot = []
for i in range(K): # 2와 6이 맞닿음
    rot.append(list(map(int, stdin.readline().split())))


def rot_gear(num, direction, visited):
    if visited[num]:
        return
    if 0 < num < T + 1:
        visited[num] = True
        if num - 1 > 0 and gear[num - 1][2] != gear[num][6]:
            rot_gear(num - 1, direction * -1, visited)
        if num + 1 < T + 1 and gear[num][2] != gear[num + 1][6]:
            rot_gear(num + 1, direction * -1, visited)

        if direction == 1:
            abc = gear[num].pop()
            gear[num].insert(0, abc)
        else:
            abc = gear[num].pop(0)
            gear[num].append(abc)

for n, d in rot:
    rot_gear(n, d, [False] * (T + 1))

ans = 0
for i in range(1, T + 1):
    if gear[i][0] == 1:
        ans += 1

print(ans)