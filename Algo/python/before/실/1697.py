# from collections import deque

# def bfs(n, k):
#     q = deque()
#     q.append(n)
#     while True:
#         x = q.popleft()
#         if x == k:
#             print(arr[x])
#             break
#         for i in (x-1, x+1, x*2):
#             if 0<=i<=100000 and arr[i] == 0:
#                 q.append(i)
#                 arr[i] = arr[x] + 1

# n, k = map(int, input().split())
# arr = [0]*100001    # visited + 깊이 저장
# bfs(n, k)


def f(n, k):
    if n>=k:                                    # 왼쪽에 있으면 -만 가능
        return n-k
    elif k==1:                                  # 0, 1 인경우
        return 1
    elif k%2:                                   # k가 홀수라면
        return min(f(n, k+1), f(n, k-1)) + 1    # +, - 중 작은거로 / 횟수 1회증가
    else:                                       # k가 짝수라면
        return min(k-n, f(n, k//2)+1)           # 

n, k = map(int,input().split())
print(f(n, k))