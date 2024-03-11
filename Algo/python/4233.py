def isprime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1
#
#
# while True:
#     p, a = map(int, input().split())
#     if p == 0 and a == 0:
#         break
#     if pow(a, p, p) == a and isprime(p):
#         print('yes')
#     else:
#         print('no')