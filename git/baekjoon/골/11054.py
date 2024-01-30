n = int(input())
a = list(map(int, input().split()))

up = [1]*n
down = [1]*n

for i in range(1,n):
    for j in range(i):
        if a[i]>a[j]:
            up[i] = max(up[i], up[j]+1)

a.reverse()
for i in range(1,n):
    for j in range(i):
        if a[i]>a[j]:
            down[i] = max(down[i], down[j]+1)
down.reverse()

bitonic = up[0]+down[0]
for i in range(1,n):
    bitonic = max(bitonic, up[i]+down[i])

print(bitonic-1)