from sys import stdin

N = int(input())
nums = list(map(int, stdin.readline().split()))
M = int(input())
nums2 = list(map(int, stdin.readline().split()))

exi = {}
#nums.sort()

for i in nums:
    if i in exi.keys():
        exi[i] += 1
    else:
        exi[i] = 1

for i in nums2:
    if i in exi.keys():
        print(exi[i], end=' ')
    else:
        print(0, end=' ')
