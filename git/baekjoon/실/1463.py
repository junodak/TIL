def cal(n):
    dp = [0]*(n+1)
    dp[2] = 1
    dp[3] = 1

    for i in range(4,n+1):
        check = [dp[i-1]+1]
        if i%3==0:
            check.append(dp[i//3]+1)
        if i%2==0:
            check.append(dp[i//2]+1)
        dp[i] = min(check)
    
    return dp[n]

n = int(input())
if n==1:
    print(0)
elif n==2:
    print(1)
elif n==3:
    print(1)
else:
    print(cal(n))