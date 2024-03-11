def cost(old, new):
    if old == new:          # 같은거 밟으면 cost 1
        return 1
    elif old * new == 0:    # 둘중 하나라도 0이라면 cost 2
        return 2
    elif abs(old-new) == 2: # 맞은편은 cost 4
        return 4
    else:                   # 아니면 cost 3
        return 3

order = list(map(int, input().split()))
MAX = len(order)*4          # 최대로 나올 수 있는 결과 보다 큼 (전부 cost 4인 경우)
dp = [[[MAX]*5 for _ in range(5)] for _ in range(2)]
dp[0][0][0] = 0             # 초깃값 0,0


same_cnt = 0
idx1, idx2 = 0, 1
for idx, n in enumerate(order):
    if order[idx] == order[idx-1]:  # 같다면 1만 추가
        same_cnt += 1
    elif n:
        idx1, idx2 = idx2, idx1
        for i in range(5):
            for j in range(5):
                dp[idx1][n][i] = min(dp[idx1][n][i], dp[idx2][j][i] + cost(j,n))
                dp[idx1][i][n] = min(dp[idx1][i][n], dp[idx2][i][j] + cost(j,n))
        for i in range(5):
            for j in range(5):
                dp[idx2][i][j] = MAX  # dp 초기화, 연산증가, 메모리 감소
    else:
        step = order[-2]              # 마지막으로 밟은거
        end_cost = MAX
        for i in range(5):
            end_cost = min(end_cost, dp[idx1][step][i], dp[idx1][i][step])
        print(end_cost + same_cnt)


# idx1, idx2 = 0, 1
# for idx, n in enumerate(order):
#     if n:
#         if order[idx] == order[idx-1]:
#             for i in range(5):
#                 dp[idx+1][n][i] = dp[idx][n][i] + 1
#                 dp[idx+1][i][n] = dp[idx][i][n] + 1
#             continue
#         else:
#             for i in range(5):
#                 for j in range(5):
#                     dp[idx+1][n][i] = min(dp[idx+1][n][i], dp[idx][j][i] + cost(j,n))
#                     dp[idx+1][i][n] = min(dp[idx+1][i][n], dp[idx][i][j] + cost(j,n))
#     else:
#         step = order[idx-1]
#         end_cost = MAX
#         for i in range(5):
#             end_cost = min(end_cost, dp[idx][step][i], dp[idx][i][step])
#         print(end_cost)