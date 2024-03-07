import sys
input = sys.stdin.readline

n = input()
arr = list(map(int, input().split()))
for i in range(int(input())):
    q = list(map(int, input().split()))
    if q[0] == 2:
        cnt = 0
        for j in range(q[1], q[2]+1):
            if arr[j-1] > q[3]:
                cnt += 1
        print(cnt)
    else:
        arr[q[1]-1] = q[2]
