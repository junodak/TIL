N=int(input())-2
dp =[[[0]*6 for _ in range(6)] for _ in range(N+1)]
ans=0

def dice_to_money(i,j,k):
    if i == j == k:
        return 10000 + (k + 1) * 1000
    elif i == j:
        return 1000 + (j + 1) * 100
    elif i == k:
        return 1000 + (k + 1) * 100
    elif j == k:
        return 1000 + (k + 1) * 100
    else:
        return (max([i, j, k]) + 1) * 100


for n in range(N):
    for i in range(6):
        for j in range(6):
            for k in range(6):
                value = dice_to_money(i,j,k)
                expect_value = dp[n][j][k]/6
                if expect_value < value or n==N:
                    dp[n+1][i][j] += dice_to_money(j,i,k)
                else:
                    dp[n+1][i][j] += expect_value

for i in range(6):
    for j in range(6):
        ans+=dp[N][i][j]
print(ans/216)