import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    order = input().split()
    if order[0] == 'push':
        arr.append(int(order[1]))
    elif order[0] == 'pop':
        if len(arr):
            print(arr.pop())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(arr))
    elif order[0] == 'empty':
        if len(arr):
            print(0)
        else:
            print(1)
    elif order[0] == 'top':
        if len(arr):
            print(arr[-1])
        else:
            print(-1)
        