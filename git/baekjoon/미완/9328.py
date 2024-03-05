import sys
sys.stdin = open('input.txt')
from collections import deque
import copy

dt = [(-1, 0), (1, 0), (0, -1), (0, 1)]

tc = int(input())
for _ in range(tc):

    # arr, key 입력
    hi, wi = map(int, input().split())
    arr = [['.']*(wi+2) for _ in range(hi+2)]
    for i in range(1, hi+1):
        arr[i][1:wi+1] = list(input())
    ky = list(input())

    cnt = 0
    check_lower = True
    while check_lower:
        copy_arr = copy.deepcopy(arr)
        que = deque()
        que.append((0, 0))
        copy_arr[0][0] = 1
        check_lower = False
        cnt = 0
        while que:
            di, dj = que.popleft()
            for dtx, dty in dt:
                dx = di + dtx
                dy = dj + dty
                if 0 <= dx < hi and 0 <= dy < wi:
                    tmp = copy_arr[dx][dy]
                    if tmp != 1 and tmp !='*':
                        if tmp == '.':
                            copy_arr[dx][dy] = 1
                            que.append((dx, dy))
                        elif tmp in ky:
                            copy_arr[dx][dy] = 1
                            que.append((dx, dy))
                        elif tmp == '$':
                            cnt += 1
                        elif tmp.islower():
                            ky.append(tmp)
                            check_lower = True
    print(cnt)
