n = int(input())
a = list(map(int, input().split()))

seq = [1]*n

for i in range(1,n):
    for j in range(i):
        if a[i]>a[j]:
            seq[i] = max(seq[i], seq[j]+1)

max_count = max(seq)
print(max_count)
subseq = []
while max_count:
    if max_count == seq[-1]:
        subseq.append(a[len(seq)-1])
        seq.pop()
        max_count -= 1
    else:
        seq.pop()
subseq.reverse()
print(*subseq)