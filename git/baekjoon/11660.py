n, m = map(int, input().split())

table = []
for i in range(n):
    table.append(list(map(int, input().split())))

dp1 = [[0]*n for _ in range(n)]
dp2 = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        dp1[i][j] += sum(dp1[i][j:])

print(table)
print(dp1)
