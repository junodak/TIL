# n = int(input())
# i = 1
# numbers = []

# while n != 1:
#     i += 1
#     if n % i == 0:
#         numbers.append(i)
#         n //= i
#         i = 1

# print(numbers)

import math

def prime_factors(n):
    factors = []
    # 2로 나누어 떨어지는 모든 소인수를 찾음
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # 이후 홀수 소수들로 나누어 떨어지는 소인수를 찾음
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    # n이 소수인 경우도 고려
    if n > 2:
        factors.append(n)
    return factors

n = int(input())
factors = prime_factors(n)
for factor in factors:
    print(factor)