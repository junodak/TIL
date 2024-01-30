n = int(input())
a = list(map(int, input().split()))

seq = [1]*n

for i in range(1,n):
    for j in range(i):
        if a[i]>a[j]:
            seq[i] = max(seq[i], seq[j]+1)

print(seq)