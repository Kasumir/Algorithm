from sys import stdin
N, M = map(int, stdin.readline().split())
tree = []
MAX = 0

tree = list(map(int, stdin.readline().split()))
for i in tree:
    if i > MAX:
        MAX = i


def cut(x):
    ret = 0
    for i in tree:
        if i > x:
            ret += (i - x)
    return ret

def binary_search():
    L = 1
    R = MAX
    ans = 0
    while L <= R:
        now = int((L + R) / 2)
        res = cut(now)
        if res >= M:
            ans = now
            L = now + 1
        else:
            R = now - 1
    return ans

print(binary_search())