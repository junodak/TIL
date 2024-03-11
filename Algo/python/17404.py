n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0]*3 for _ in range(3)] for _ in range(n)]

for i in range(3):
    for j in range(3):
        dp[0][j][i] = 1000001
    dp[0][i][i] = rgb[0][i]

for i in range(1, n):
    for j in range(3):
        dp[i][0][j] = rgb[i][0] + min(dp[i-1][1][j], dp[i-1][2][j])
        dp[i][1][j] = rgb[i][1] + min(dp[i-1][0][j], dp[i-1][2][j])
        dp[i][2][j] = rgb[i][2] + min(dp[i-1][0][j], dp[i-1][1][j])

a = dp[n-1]
print(min(a[1][0], a[2][0], a[0][1], a[2][1], a[0][2], a[1][2]))
