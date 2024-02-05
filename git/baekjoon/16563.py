import math
import sys
input = sys.stdin.readline

def prime(n):
    arr = []
    # 2로 나누어 떨어지는 모든 소인수를 찾음
    while n % 2 == 0:
        arr.append(2)
        n //= 2
    # 이후 홀수 소수들로 나누어 떨어지는 소인수를 찾음
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            arr.append(i)
            n //= i
    # n이 소수인 경우도 고려
    if n > 2:
        arr.append(n)
    return arr

t = int(input())
num = list(map(int,input().split()))
for i in range(t):
    arr = prime(num[i])
    print(*arr)