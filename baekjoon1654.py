from sys import stdin

K, N = map(int, stdin.readline().split())
LenCable = []
MAX = 0
for _ in range(K):
    tmp = int(input())
    if tmp > MAX:
        MAX = tmp
    LenCable.append(tmp)

def cut(x):
    ret = 0
    for i in LenCable:
        ret += int(i / x)
    return ret

def binary_search():
    L = 1
    R = MAX
    ans = 0
    while L <= R:
        now = int((L + R) / 2)
        res = cut(now)
        if res >= N:
            ans = now
            L = now + 1
        elif res < N:
            R = now - 1
    return ans

print(binary_search())


