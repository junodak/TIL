n = int(input())
arr = list(map(int, input().split()))
arr.sort()
scope = 0
if arr[0] == 1:
    scope = 1
    for i in range(1, n):
        if scope+1 >= arr[i]:
            scope += arr[i]
        else:
            break
print(scope+1)