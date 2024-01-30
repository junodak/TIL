n, k = list(map(int, input().split()))
coin = [0]*n
for i in range(n):
    coin[i] = int(input())

state = 0
for i in range(n):
    if coin[i] <= k:
        state = i
    else:
        break

count = 0
for i in range(state,-1,-1):
    count += k//coin[i]
    k %= coin[i]

print(count)