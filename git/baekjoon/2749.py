n = int(input())
arr = [0,1,1]

for i in range(n-1):
    arr[2] = arr[0] + arr[1]
    arr[0] = arr[1]
    arr[1] = arr[2]

if n:
    print(arr[1])
else:
    print(0)