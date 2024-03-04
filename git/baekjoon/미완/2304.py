n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
arr.sort()
print(arr)

for i in range(n):
    arr[i][]