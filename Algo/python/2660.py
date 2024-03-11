n = int(input())
arr = []
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    if a < b:
        arr.append([a, b])
    else:
        arr.append([b, a])

print(arr)