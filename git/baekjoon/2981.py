# n = int(input())
# num = [0]*n
# for i in range(n):
#     num[i] = int(input())

# num.sort()
# remain = num[1]-num[0]

# for i in range(2,n):
#     remain = min(remain, num[i]-num[i-1])

# result = []
# for i in range(2, remain+1):
#     if remain % i == 0:
#         result.append(i)

# print(*result)

from math import gcd

n=int(input())
M = []
minus = []
for _ in range(n):
    M.append(int(input()))
for i in range(n-1):
    minus.append(M[i+1] - M[i])
gcm = gcd(*minus)
result = []
for j in range(2,int(gcm**0.5+1)):
    if gcm % j == 0:
        result += [j]
        result += [gcm//j]
result += [gcm]
result = list(set(result))
result.sort()
print(*result)
