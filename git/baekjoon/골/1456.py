import math

def primes(n):
    arr = [0, 0] + [1]*(n-1)
    for i in range(2, int(n ** 0.5) + 1):
        if arr[i]:
            for j in range(i*i, n+1, i):
                arr[j] = 0
    return [i for i in range(2, n + 1) if arr[i]]

m, n = map(int, input().split())
arr = primes(int(n**0.5))
cnt_n = [0]*len(arr)
for i in range(len(arr)):
    cnt_n[i] += int(math.log(n, arr[i])) - 1  # 1제곱을 제외하고 제곱수 저장
    for j in range(2, cnt_n[i]+2):
        if arr[i]**j < m:
            cnt_n[i] -= 1
        else:
            break

print(sum(cnt_n))