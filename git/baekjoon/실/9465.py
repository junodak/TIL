t = int(input())
for _ in range(t):
    n = int(input())
    sticker = []
    for i in range(2):
        sticker.append(list(map(int, input().split())))
    if n==1:
        print(*max(sticker))
    else :
        sticker[0][1] += sticker[1][0]
        sticker[1][1] += sticker[0][0]
        for i in range(2,n):
            sticker[0][i] += max(sticker[1][i-1], sticker[1][i-2])
            sticker[1][i] += max(sticker[0][i-1], sticker[0][i-2])
            
        print(max(sticker[0][n-1],sticker[1][n-1])) 


    # if n%2:
    #     for i in range(0,n-2,2):
    #         sticker[0][i+2] += max(sticker[1][i], sticker[0][i]+sticker[1][i+1])
    #         sticker[1][i+2] += max(sticker[0][i], sticker[1][i]+sticker[0][i+1])
    # else:
    #     sticker[0][1] += sticker[1][0]
    #     sticker[1][1] += sticker[0][0]
    #     for i in range(1,n-1,2):
    #         sticker[0][i+2] += max(sticker[1][i], sticker[0][i]+sticker[1][i+1])
    #         sticker[1][i+2] += max(sticker[0][i], sticker[1][i]+sticker[0][i+1])