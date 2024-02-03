

m, n = map(int, input().split())

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(m, n + 1):
    if is_prime(i):
        print(i)


# def sieve_of_eratosthenes(n):
#     primes = [True] * (n + 1)
#     primes[0] = primes[1] = False

#     for i in range(2, int(n ** 0.5) + 1):
#         if primes[i]:
#             for j in range(i * i, n + 1, i):
#                 primes[j] = False

#     return [i for i in range(2, n + 1) if primes[i]]

# # Example usage:
# n = 100
# print(sieve_of_eratosthenes(n))
        
def sieve_of_eratosthenes(n):
    primes = [1] * (n + 1)
    primes[0] = primes[1] = 0

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = 0

    return [i for i in range(2, n + 1) if primes[i]]

# Example usage:
n = 100
print(sieve_of_eratosthenes(n))

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return [i for i in range(2, n + 1) if primes[i]]

# Example usage:
n = 100
print(sieve_of_eratosthenes(n))


m, n = map(int, input().split())
sieve = [True] * (n+1)
sieve[0] = sieve[1] = False

for i in range(2, int(n**0.5)+1):
    if sieve[i]:
        for j in range(i*i, n+1, i):
            sieve[j] = False

for i in range(m, n+1):
    if sieve[i]:
        print(i)
