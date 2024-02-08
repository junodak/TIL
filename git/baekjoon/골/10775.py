import sys
input = sys.stdin.readline

def dock(num):
    real_num = num - dp[num]
    while gate[real_num]:
        real_num -= 1
        dp[num] += 1
    if real_num==0:
        return False
    else:
        gate[real_num] = 1
        return True

g = int(input())
gate = [0]*(g+1)
dp = [0]*(g+1)
p = int(input())
dock_count = 0
for i in range(p):
    n = int(input())
    if dock(n):
        dock_count += 1
    else:
        break

print(dock_count)