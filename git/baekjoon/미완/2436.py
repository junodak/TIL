# import sys
# input = sys.stdin.readline

# def primes(n):
#     arr = [0,0] + [1]*(n-1)
#     lst = [0]

#     for i in range(2, int(n ** 0.5) + 1):
#         if arr[i]:
#             for j in range(i*i, n+1, i):
#                 arr[j] = 0
    
#     return [i for i in range(n+1) if arr[i]]


# t = int(input())
# k = list(map(int, input().split()))
# arr = primes(int(max(k) ** 0.5) + 1)

# for i in range(t):
#     prime = 0
#     arr2 = []
#     while k[i]>1 and len(arr):
#         if k[i] % arr[prime] == 0:
#             k[i] //= arr[prime]
#             arr2.append(arr[prime])
#         else:
#             prime += 1
#     if k[i] > 1:
#         arr2.append(k[i])
#     print(*arr2)

import sys
input = sys.stdin.readline

def primes(n):
    arr = [0,0] + [1]*(n-1)
    lst = [0]

    for i in range(2, int(n ** 0.5) + 1):
        if arr[i]:
            for j in range(i*i, n+1, i):
                arr[j] = 0
    
    return [i for i in range(n+1) if arr[i]]

t = int(input())
k = list(map(int, input().split()))
arr = primes(int(max(k) ** 0.5) + 1)

for i in range(t):
    prime = 0
    arr2 = []
    while k[i] > 1 and prime < len(arr):
        if k[i] % arr[prime] == 0:
            k[i] //= arr[prime]
            arr2.append(arr[prime])
        else:
            prime += 1
    if k[i] > 1:
        arr2.append(k[i])
    print(*arr2)
