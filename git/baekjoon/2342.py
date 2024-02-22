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

order = list(map(int, input().split()))
length = len(order)
MAX = length*4
dp = [[[MAX]*5 for _ in range(5)] for _ in range(length)]

for i in range(length):
    for left in range(5):
        for right in range(5):
            dp[left][right][i] = min(dp[order[i]][right][i+1], dp[left][order[i]][i+1])