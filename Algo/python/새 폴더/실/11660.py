import sys
input = sys.stdin.readline

n, m = map(int, input().split())

table = []
for i in range(n):
    table.append(list(map(int, input().split())))

dp_row = [[0]*(n+1) for _ in range(n)]
# dp_col = [[0]*(n+1) for _ in range(n)]

for i in range(n):
    for j in range(n):
        dp_row[i][j] = sum(table[i][j:])
#         for k in range(j,n):
#             dp_col[j][i] += table[k][i]

for i in range(m):
    x1, y1, x2, y2= map(int, input().split())

    sum = 0
    for j in range(x1-1, x2):
        sum += dp_row[j][y1-1] - dp_row[j][y2]
    print(sum)