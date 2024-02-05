def sieve_of_eratosthenes(m, n):
    primes = [1] * (n + 1)
    primes[0] = primes[1] = 0
    x = 1
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i*x):
                primes[j] = 0
            x *= i
    return [i for i in range(m, n + 1) if primes[i]]

m, n = map(int, input().split())
arr = sieve_of_eratosthenes(m, n)
for i in arr:
    print(i)
