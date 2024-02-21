
import itertools

def primes(n):
    arr = [1] * (n + 1)
    arr[0] = arr[1] = 0
    for i in range(4, n+1, 2):
        arr[i] = 0
    for i in range(3, int(n**0.5) + 1):
        if arr[i]:
            for j in range(i*i, n+1, i*2):
                arr[j] = 0
    return [i**2 for i in range(n+1) if arr[i]]

def comb(num):
    cnt = 0
    for i in itertools.combinations(arr, num):
        cnt+=1
    return cnt

n = 100
arr = list(range(1, n))
a = 0
for i in range(1, 5):
    a += comb(i)
print(a)

arr = primes(180)
print(arr)

# 31623**2 = 100000
# 아무리 많아도 6개 안넘어감

