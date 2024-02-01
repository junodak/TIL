N=int(input())-2
dp =[[[0]*6 for _ in range(6)] for _ in range(N+1)]

def money(i,j,k):
    if i==j==k:
        return 10000+(k+1)*1000
    elif i==j:
        return 1000+(i+1)*100
    elif j==k:
        return 1000+(j+1)*100
    elif k==i:
        return 1000+(k+1)*100
    else:
        return (max(i,j,k)+1)*100

for n in range(N):
    for i in range(6):
        for j in range(6):
            for k in range(6):
                new = money(i,j,k)
                old = dp[n][j][k]/6
                dp[n+1][i][j] += max(new, old)

best=0
for i in range(6):
    best+=sum(dp[N][i])
print(best/216)