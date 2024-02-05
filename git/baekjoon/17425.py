# import sys
# input = sys.stdin.readline

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     sum = n*n
#     for i in range(2,n+1):
#         sum -= n%i
#     print(sum)


# t = int(input())
# for _ in range(t):
#     n = int(input())
#     # sum = n
#     # for i in range(2,n+1):
#         # sum += i*(n//i)
#     print(sum)


def sum_of_div(n):
    result = 0
    i = 1
    while i*i <= n:
        if n % i == 0:
            result += i
            if i != n // i:
                result += n // i
        i += 1
    return result

dp = [0]
t = int(input())
for _ in range(t):
    n = int(input())
    
    if len(dp) < n+1:
        for i in range(len(dp),n+1):
            dp.append(dp[i-1] + sum_of_div(i))
    print(dp[n])