import math

def cal(n):
    root = int(math.sqrt(n)) 
    gap = n - pow(root,2)
    if gap == 0:
        time = root*2-1
    elif gap <= root:
        time = root*2
    else:
        time = root*2+1
    return time

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    print(cal(y-x))

'''
01 : 1
02 : 11
03 : 111
---
04 : 121
05 : 1211
06 : 1221
07 : 12211
08 : 12221
---
09 : 12321
10 : 123211
11 : 123221
12 : 123321
13 : 1233211
14 : 1233221
15 : 1233321
---
16 : 1234321
'''