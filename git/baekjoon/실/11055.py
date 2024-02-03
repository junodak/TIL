n = int(input())
a = list(map(int, input().split()))

seq = a[:]

for i in range(1,n):
    for j in range(i):
        if a[i]>a[j]:
            seq[i] = max(seq[i], seq[j]+a[i])

print(max(seq))