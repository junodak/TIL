# 중점 : 0
# 위 : 1
# 왼 : 2
# 아 : 3
# 오 : 4


# 0 -> (1,2,3,4) : 2
# 제자리 : 1
# 옆칸 : 3
# 맞은편 : 4

# 1 2 2 4 0

# 00, 01, 02, 03, 04
# 10, 11, 12, 13, 14
# 20, 21, 22, 23, 24
# 30, 31, 32, 33, 34
# 40, 41, 42, 43, 44

def cost(old_left, old_right, new_left, new_right):
    if old_left == new_left:
        if old_right == new_right:
            return 1
    else:


order = list(map(int, input().split()))
MAX = len(order)*5
dp = [[[MAX]*2 for _ in range(5)] for _ in range(5)]
dp[0][0][0] = 0  # 초깃값 0,0

idx1, idx2 = 1, 0
for n in order:
    idx1, idx2 = idx2, idx1
    for i in range(5):
        for j in range(5):
            dp[idx1][n][i] = min(dp[idx1][n][i], dp[idx2][j][i] + cost(j,i,n,i))
            dp[idx1][i][n] = min(dp[idx1][i][n], dp[idx2][i][j] + cost(i,j,i,n))
    for i in range(5):
        for j in range(5):
            dp[idx2][i][j] = MAX  #dp 초기화

        # dp[0][l][r] -> dp[1][n][r]
        # dp[0][l][r] -> dp[1][l][n]
        # i로 이동
            

    

    # dp[i][left][right] = min(dp[order[i-1][i]][right], dp[i+1][left][order[i]])

# 다음껄 밟아야하는데
# 왼발이 갈 수도 있고, 오른발이 갈 수도 있음
# 왼발이 간다면?