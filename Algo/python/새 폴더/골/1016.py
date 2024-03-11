def primes(m, n):
    arr = [1]*(n-m+1)
    sqt = int(n ** 0.5)
    arr2 = [0,0] + [1]*(sqt-1)

    for i in range(2, sqt + 1):
        if arr2[i]:
            for j in range(i*i, sqt+1, i):
                arr2[j] = 0
            for j in range(-m%(i*i), n-m+1, i*i):
                arr[j] = 0
    
    cnt = 0
    for i in range(n-m+1):
        if arr[i]:
            cnt += 1
    return cnt

m, n = map(int, input().split())
print(primes(m, n))