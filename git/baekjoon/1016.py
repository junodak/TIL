def primes(n):
    arr = [0,0] + [1]*(n-1)
    lst = []

    for i in range(2, int(n ** 0.5) + 1):
        if arr[i]:
            for j in range(i*i, n+1, i):
                arr[j] = 0
    
    for i in range(n+1):
        if arr[i]:
            lst.append(i)

    return lst

arr = primes(10000000)
print(len(arr))