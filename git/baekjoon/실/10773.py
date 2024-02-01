n = int(input())
arr = []
for _ in range(n):
    num = int(input())
    if num:
        arr.append(num)
    else:
        arr.pop()
print(sum(arr))
