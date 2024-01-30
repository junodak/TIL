n = int(input())

r = [0]*n
g = [0]*n
b = [0]*n

for i in range(n):
    r[i], g[i], b[i] = map(int, input().split())

dp = [[0] * 3 for _ in range(n)]

# 첫 번째 행 초기화
dp[0][0] = r[0]
dp[0][1] = g[0]
dp[0][2] = b[0]

# 두 번째 행부터는 이전 행에서 선택한 색상을 제외한 나머지 중 최소값을 선택
for i in range(1, n):
    dp[i][0] = r[i] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = g[i] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = b[i] + min(dp[i-1][0], dp[i-1][1])

# 마지막 행에서 최소값을 선택
result = min(dp[n-1])

print(result)
