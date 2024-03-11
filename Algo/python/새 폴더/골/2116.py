n = int(input())
sum = 0
dp_idx = [1,2,3,4,5,6]
dp = [0,0,0,0,0,0]

for i in range(n):
    d = list(map(int, input().split()))

    for j in range(6):
        # dp_index[j]가 밑으로 갔을 때, max를 구해서 dp[j]에 넣기
        idx = d.index(dp_idx[j])
        if idx==0 or idx==5:
            dp[j] += max(d[1],d[2],d[3],d[4])
        elif idx==1 or idx==3:
            dp[j] += max(d[0],d[2],d[4],d[5])
        else:
            dp[j] += max(d[0],d[1],d[3],d[5])

    for j in range(6):
        idx = d.index(dp_idx[j])
        if idx==0:
            dp_idx[j] = d[5]
        elif idx==1:
            dp_idx[j] = d[3]
        elif idx==2:
            dp_idx[j] = d[4]
        elif idx==3:
            dp_idx[j] = d[1]
        elif idx==4:
            dp_idx[j] = d[2]
        else:
            dp_idx[j] = d[0]

print(max(dp))




# n = int(input())
# sum = 0
# dp_idx = [1,2,3,4,5,6]
# dp = [0,0,0,0,0,0]

# for i in range(n):
#     d = list(map(int, input().split()))

#     for j in range(6):
#         # dp_index[j]가 밑으로 갔을 때, max를 구해서 dp[j]에 넣기
#         idx = d.index(dp_idx[j])
#         if idx==0 or idx==5:
#             dp[j] += max(d[1],d[2],d[3],d[4])
#         elif idx==1 or idx==4:
#             dp[j] += max(d[0],d[2],d[3],d[5])
#         else:
#             dp[j] += max(d[0],d[1],d[4],d[5])
#     for j in range(0, 6):
#         dp_idx[j] = d[5 - d.index(dp_idx[j])] # j의 반대편이 누군지

# print(max(dp))