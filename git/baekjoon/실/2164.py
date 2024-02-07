import math
n = int(input())
print(2*n - 2**math.ceil(math.log2(n)))

# arr = list(range(1,n+1))
# while len(arr)>1:
#     arr.pop(0)
#     arr.append(arr.pop(0))
# print(arr)

# 1 : 1 = 2-1
# 2 : 2 = 4-4
# 3 : 2 = 6-4
# 4 : 4 = 8-4
# 5 : 2 = 10-8
# 6 : 4 = 12-8
# 7 : 6 = 14-8
# 8 : 8 = 16-8
# 9 : 2 = 18-16
# 10: 4 = 20-16
# 11: 6 = 22-16
# 12: 8 = 24-16
# 13:10 = 26-16
# 14:12 = 28-16
# 15:14 = 30-16
# 16:16 = 32-16
