from math import gcd

n = int(input())
num = [0]*n
for i in range(n):
    num[i] = int(input())

minus = []
for i in range(n-1):
    minus.append(num[i+1] - num[i])

gcm = gcd(*minus)

result = []

for i in range(2,int(gcm**0.5+1)):
    if gcm % i == 0:
        result.append(i)
        result.append(gcm//i)
result.append(gcm)
result = list(set(result))
result.sort()
print(*result)