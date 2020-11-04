from sys import stdin

N = int(input())
nums = list(map(int, stdin.readline().split()))
M = int(input())
nums2 = list(map(int, stdin.readline().split()))

nums.sort()

def binary_search(x):
    L = 0
    R = N - 1

    while L <= R:
        tmp = int((L + R) / 2)
        #print(tmp)
        if x == nums[tmp]:
            return True
        elif x < nums[tmp]:
            R = tmp - 1
        elif x > nums[tmp]:
            L = tmp + 1

    return False

for i in nums2:
    if binary_search(i):
        print(1)
    else:
        print(0)