arr = list(range(0, 10))
for i in range(1 << 10):
    for j in range(10):
        if i & (1 << j):
            print(arr[j], end='')
    print()



# n = int(input())
# res = 0
# for _ in range(n):
#     res += 1
#     while True:
#         temp = str(res)
#         len_temp = len(temp)
#         check = False
#         for i in range(len_temp):
#             for j in range(i+1, len_temp):
#                 if int(temp[i]) <= int(temp[j]):
#                     check = True
#         if check:
#             res += 1
#         else:
#             break
# print(res)





# n = int(input())
#
# check = [0, 9, 45, 120, 210, 252, 210, 120, 45, 10, 1]
#
# map = [
# [1, 1, 1, 1, 1, 1, 1, 1, 1],
# [1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 3, 6, 10, 15, 21, 28, 36],
# [0, 0, 1, 4, 10, 20, 35, 56, 84],
# [0, 0, 0, 1, 5, 15, 35, 70, 126],
# [0, 0, 0, 0, 1, 6, 21, 56, 126],
# [0, 0, 0, 0, 0, 1, 7, 28, 84],
# [0, 0, 0, 0, 0, 0, 0, 1, 8, 36],
# [0, 0, 0, 0, 0, 0, 0, 1, 9],
# [0, 0, 0, 0, 0, 0, 0, 0, 1]
# ]
#
# for i in range(1,11):
#     if sum(check[:i]) < n and  n <= sum(check[:i+1]):
#         print(map[i-1])
#         n -= sum(check[:i])
#         print('남은거 :',n)
#
#         for j in range(10):
#             if n>map[i-1][j]:
#                 n-=map[i-1][j]
#             else:
#                 print(j+1, end='')
#                 for k in range(10):
#                     if n>map[i-2][k]:
#                         n-=map[i-2][k]
#                     else:
#                         print(k+1, n-1)
#                         break
#                 break
                


# 18 : 42
# 9+6+3(40+2)


# 9번쨰 : 9
# 9+45번쨰 : 98
# 9+45+120번쨰 : 987
# 9+45+120+210번쨰 : 9876
# 9+45+120+210+252번쨰 : 98765
# 9+45+120+210+252+210번쨰 : 987654
# 9+45+120+210+252+210+120번쨰 : 9876543
# 9+45+120+210+252+210+120+45번쨰 : 98765432
# 9+45+120+210+252+210+120+45+10번쨰 : 987654321
# 9+45+120+210+252+210+129+45+10+1번쨰 : 9876543210