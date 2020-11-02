from sys import stdin
T = int(stdin.readline())
ans = []
for _ in range(T):
    N, M = map(int, stdin.readline().split())
    for _ in range(M):
        stdin.readline()
    ans.append(N - 1)
for i in ans:
    print(i)