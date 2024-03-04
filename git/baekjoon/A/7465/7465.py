from collections import deque
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    matrix = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
    for _ in range(m):
        p1, p2 = map(int, input().split())
        matrix[p1-1][p2-1] = 1
        matrix[p2-1][p1-1] = 1

    visited = [0]*(n+1)
    cnt = 0
    for i in range(n):
        if visited[i] == 0:
            q = deque()
            q.append(i)
            visited[i] = 1
            while q:
                x = q.popleft()
                for j in range(n):
                    if matrix[x][j] and visited[j] == 0:
                        q.append(j)
                        visited[j] = 1
            cnt += 1
    print(f'#{tc} {cnt}')
