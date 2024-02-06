# # ---- 1번 ----
# n = int(input())
# sum = n*n
# for i in range(2,n+1):
#     sum -= n%i
# print(sum)

# n = int(input())
# sum = 0
# for i in range(1, n+1):
#     sum += n//i*i
# print(sum)


# n = int(input())
# print(sum(n//k*k for k in range(1,n+1)))

# a, b = divmod(10,3)
# print(b)

# # ---- 2번 ----

# def sum_of_div(n):
#     result = 0
#     i = 1
#     while i*i <= n:
#         if n % i == 0:
#             result += i
#             if i != n // i:
#                 result += n // i
#         i += 1
#     return result

# dp = [0]
# n = int(input())

# if len(dp) < n+1:
#     for i in range(len(dp),n+1):
#         dp.append(dp[i-1] + sum_of_div(i))
# print(dp[n])

# # 약수를 구하고, 구하는 즉시 합을 더함

# t = int(input())
# k = list(map(int, input().split()))
# arr = primes(int(max(k) ** 0.5) + 1)

# for i in range(t):
#     prime = 0
#     arr2 = []
#     while k[i] > 1 and prime < len(arr):
#         if k[i] % arr[prime] == 0:
#             k[i] //= arr[prime]
#             arr2.append(arr[prime])
#         else:
#             prime += 1
#     if k[i] > 1:
#         arr2.append(k[i])
#     print(*arr2)

# # --------------------------------
# import sys
# input = sys.stdin.readline

# def primes(n):
#     arr = [0, 0] + [1]*(n-1)
#     for i in range(2, int(n ** 0.5) + 1):
#         if arr[i]:
#             for j in range(i*i, n+1, i):
#                 arr[j] = 0
#     return [i for i in range(2, n + 1) if arr[i]]

# def find_factor(arr, n):
#     prime_mul = 1
#     for i in arr:
#         prime_sum = 1
#         prime_cnt = 1
#         while n%i == 0:  # 나머지가 나올때까지 나누기
#             n //= i
#             prime_sum += i**prime_cnt
#             prime_cnt += 1
#         prime_mul *= prime_sum
#         if n==1:
#             break
#     if n!=1: # arr 전부 돌아도 n이 1이 아니면 그 수가 소수
#         prime_mul *= (n+1)
#     return prime_mul

# # t = int(input())
# # arr = primes(1000)
# for tc in range(t):
#     sum_factor = 0
#     n = int(input())
#     for i in range(1,n+1):
#         sum_factor += find_factor(arr,i)
#     print(sum_factor)

    
# # --------------------------------

def primes(n):
    arr = [0, 0] + [1]*(n-1)
    for i in range(2, int(n ** 0.5) + 1):
        if arr[i]:
            for j in range(i*i, n+1, i):
                arr[j] = 0
    return [i for i in range(2, n + 1) if arr[i]]


arr = primes(1000)
arr2 = [0]*len(arr)
for i in range(len(arr)):
    while 
    arr[i]