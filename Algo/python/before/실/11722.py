n = int(input())
a = list(map(int, input().split()))

down = [1]*n

a.reverse()
for i in range(1,n):
    for j in range(i):
        if a[i]>a[j]:
            down[i] = max(down[i], down[j]+1)

print(max(down))