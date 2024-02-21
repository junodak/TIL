import itertools

# 에라토스테네스 체를 이용하여 소수의 제곱수 list 구하기, 20억 : 5000개미만
def primes(n):
    arr = [1] * (n + 1)
    arr[0] = arr[1] = 0
    for i in range(4, n+1, 2):
        arr[i] = 0
    for i in range(3, int(n**0.5) + 1):
        if arr[i]:
            for j in range(i*i, n+1, i*2):
                arr[j] = 0
    return [i**2 for i in range(n+1) if arr[i]]


# n보다 작고, n과 가장 가까운 제곱 ㄴㄴ수 구하기
def find_not_pow(n):
    check = False
    for i in arr:
        if n % i == 0:      # 제곱수에 나눠지면 -1 해서 다시
            check = True
            break
        if n < i:           # i가 더 크면 더 계산 필요없음
            break
    if check:
        n = find_not_pow(n-1)
    return n


def comb(n, num):
    sum_cnt = 0
    check = True
    for i in itertools.combinations(arr, num):
        if check:
            temp = 1
            for j in i:
                temp *= j
                if temp > n:
                    check = False
                    break
            sum_cnt += (n // temp)
    return sum_cnt


# n은 몇 번째 제곱 ㄴㄴ수인지, 포함배제
def not_pow_cnt(n, p_cnt):
    # n까지 제곱수의 배수의 개수를 구하고, 그 개수를 n에서 뺀다.
    cnt = 0
    # 1개일때, 2개일때, 3개일때, 4개일때 , ... , len(arr)개일때
    for i in range(1, p_cnt+1):
        if i%2: # 홀수개일때는 더하고
            cnt += comb(n, i)
            # cnt += seq(n, i, p_cnt)
        else:   # 짝수개일때는 빼기
            cnt -= comb(n, i)
            # cnt -= seq(n, i, p_cnt)
    return n - cnt


# 이진탐색
def bin_search(l, r, p_cnt):
    mid = (l+r)//2
    mid = find_not_pow(mid)
    a = not_pow_cnt(mid, p_cnt)         # mid는 a번째 제곱ㄴㄴ수
    if k == a:                          # mid가 k번째 제곱ㄴㄴ수이면
        result = mid
    elif k > a:                         # k번째 제곱ㄴㄴ수가 mid보다 크다면
        result = bin_search(mid+1, r, p_cnt)     # 우측 이진탐색
    else:
        result = bin_search(l, mid-1, p_cnt)
    return result

# k <= 10억 // 10억 번째 제곱ㄴㄴ수 : 16억~17억
k = int(input())
arr = primes(int((k*2)**0.5))
p_cnt = len(arr)    # 제곱수 개수 : 5000개 미만

# k번째 제곱 ㄴㄴ수는 k와 2k 사이에 있다고 가정하고 이진탐색
if k < 1000:
    result = bin_search(k, k*2, p_cnt)
else: # 1000보다 커지면 더 정교하게 이진탐색
    result = bin_search(int(k*1.6), int(k*1.7), p_cnt)
print(result)



# a,b=map(int,input().split())
# for i in itertools.combinations(sorted(map(int,input().split())),b):
#     print(*i)

# import itertools
# n,m=map(int,input().split())

# arr = list(map(int,input().split()))
# arr.sort()
# [print(*i) for i in itertools.combinations(arr,m)]

# # arr에서 num개를 골라서 전부 곱한것을 n에 나눈 몫들의 합 반환
# def seq(n, num, p_cnt, level = 0, sum_cnt = 0, stack = []):
#     if level == num:
#         temp = 1
#         for i in stack:
#             temp *= i
#         sum_cnt += (n // temp)

#     for i in range(p_cnt):
#         if any(x >= arr[i] for x in stack): continue
#         stack.append(arr[i])
#         sum_cnt = seq(n, num, p_cnt, level + 1, sum_cnt, stack)
#         stack.pop()
    
#     return sum_cnt

# K번째 제곱ㄴㄴ수
# 4의 배수 - 36의배수 - 100의 배수 + 900의 배수
# 9의 배수 - 225의배수
# 25의배수

# 100번째 제곱 ㄴㄴ수를 구하시오
# 200에서 4, 9, 25, 49, 121, 169 의 배수를 걸러야한다.

# 200 // 4 = 50
# 200 // 9 = 22
# 200 // 25 = 8
# 200 // 49 = 4
# 200 // 121 = 1
# 200 // 169 = 1

# 200 // 36 = 5
# 200 // 100 = 2
# 200 // 196 = 1


# 2  : 4    2*2*1       2*2*2           4 8 12 16 20 24 28 32 ~~~
# 3  : 9    3*3*1       3*3*2           9 18 27 X 45 54 63 X 81
# 5  : 25   5*5*1       5*5*2           25 50 100 X 125 150 175 X X
# 7  : 49   7*7*1       7*7*2           49 98 147 X
# 11 : 121  9*9*1       9*9*2           121
# 13 : 169  13*13*1     13*13*2         169
# 17 : 289  17*17*1     17*17*2
# 19 : 361  19*19*1     19*19*2
# 23 : 529  23*23*1     23*23*2
# 29 : 841  29*29*1     29*29*2
# 31 : 961  31*31*1     31*31*2


# 4의 배수 + 9의 배수 - 36의 배수
# 4의 배수 + 9의 배수 + 25의 배수 - 36의배수 - 100의 배수 - 225의 배수 + 900의 배수

# 4의배수 - 36의배수 - 100의 배수 + 900의 배수
# 9의 배수 - 225의배수
# 25의 배수

# 4의배수(9,25의 배수라면 미포함), 9의배수(25의 배수라면 미포함), 25의 배수
# 4의배수 : 4, 8, 16, 20, 24, 28, 32, X, 40, 44, 48, 52, 56, 60, 64, 68, X, 76, 80, 84, 88, 92, 96, X, 104, X
# 9의배수 : 9, 18, 27, 36, 45, 54, 63, 72 ,81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180
# 25의 배수 : 25, 50, 75, 100, 125, 150



# 4, 9, 25, 49

# 4의배수 - 36의배수 - 100의 배수 - 4*49의 배수 + 

# A, B, C
# AB, AC, BC
# ABC
# A U B U C
# = A + B + C - AB - AC - BC + ABC

# A, B, C, D
# A, B, C
# AB, AC, AD, BC, BD, CD
# ABC, ABD, ACD, BCD
# ABCD
# A U B U C U D
# = A + B + C + D - AB - AC - AD - BC - BD - CD + ABC + ABD + ACD + BCD - ABCD
# = (A - AB - AC - AD + ABC + ABD + ACD - ABCD) + (B - BC - BD + BCD) + (C - CD) + (D)