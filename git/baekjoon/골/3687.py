# dp = [0]*101
# for i in range(2,101):
#     if i%7==0:
#         dp[i] = ''+'8'*(i//7)
#     elif i%7==1:
#         dp[i] = '10'+'8'*(i//7-1)
#     elif i%7==2:
#         dp[i] = '1'+'8'*(i//7)
#     elif i%7==3:
#         dp[i] = '7'+'8'*(i//7)
#         dp[i] = dp[i].replace('78','22')
#         dp[i] = dp[i].replace('28','00')
#     elif i%7==4:
#         dp[i] = '4'+'8'*(i//7)
#         dp[i] = dp[i].replace('48','20')
#     elif i%7==5:
#         dp[i] = '2'+'8'*(i//7)
#     elif i%7==6:
#         dp[i] = '6'+'8'*(i//7)

n = int(input())
for i in range(n):
    stick = int(input())
    if stick%2:
        max = '7'+'1'*(stick//2-1)
    else:
        max = '1'*(stick//2)
    
    min_arr = ['','10','1','7','4','2','6']
    min = min_arr[stick%7]
    if stick%7==1:
        min += '8'*(stick//7-1)
    else:
        min += '8'*(stick//7)
    if stick%7==3:
        min = min.replace('78','22')
        min = min.replace('28','00')
    if stick%7==4:
        min = min.replace('48','20')

    print(min, max)






        # 3 : 7, 78, 788, 7888, 78888
        # 3 : 7, 22, 228, 2288, 22888 : 78 -> 22
        # 3 : 7, 22, 200, 2008, 20088 : 28 -> 00
        # 4 : 4, 48, 488, 4888, 48888
        # 4 : 4, 20, 208, 2088, 20888 : 48 -> 20