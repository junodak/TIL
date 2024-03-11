N = 1000001
n = int(input())
arr = list(map(int, input().split()))

cnt = [0]*N
for i in arr:
    cnt[i] = 1

score = [0]*N
for i in range(N):
    if cnt[i]:
        for j in range(i*2, N, i):
            if cnt[j]:
                score[i] += 1
                score[j] -= 1

for i in arr:
    print(score[i], end=' ')
print()
