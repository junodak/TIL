from collections import deque
import copy
import sys
sys.stdin = open('input.txt')

dt = [(-1, 0), (1, 0), (0, -1), (0, 1)]

tc = int(input())
for _ in range(tc):

    # arr, key 입력
    hi, wi = map(int, input().split())
    arr = [['.']*(wi+2) for _ in range(hi+2)]
    for i in range(1, hi+1):
        arr[i][1:wi+1] = list(input())
    ky = list(input())

    for i in arr:
        print(*i)
    print(ky)

    que = deque
    que.append((0, 0))
    arr[0][0] = 1
    while que:
        di, dj = que.popleft()
        for dtx, dty in dt:
