
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))


# n = 7
# arr = [5,4,3,7,1,2,6]

# n = 10000
# arr = list(range(10000, 0, -1))

min, max = 1, n

for i in range(1,n+1):
    if i%2:
        idx = arr.index(min)
        print(idx)
        arr.pop(idx)
        arr.reverse()
        min += 1
    else:
        idx = arr.index(max)
        print(idx)
        arr.pop(idx)
        arr.reverse()
        max -= 1

# input이 10만개일때 발생할 수있는 시간초과 고려 필요, 제한시간 1초
# index? reverse?, pypy로 해결
        
# 5 4 3 7 1 2 6 : ----------- | 1은 앞에서 4번째, 1pop, 5 4 3 7 2 6
# 1 5 4 3 7 2 6 : 1이 4번 이동 | 7은 뒤에서 2번째, 7pop, 5 4 3 2 6
# 1 5 4 3 2 6 7 : 7이 2번 이동 | 2는 앞에서 3번째, 2pop, 5 4 3 6
# 1 2 5 4 3 6 7 : 2가 3번 이동 | 6은 뒤에서 0번째, 6pop, 5 4 3
# 1 2 5 4 3 6 7 : 6이 0번 이동 | 3은 앞에서 2번째, 3pop, 5 4
# 1 2 3 5 4 6 7 : 3이 2번 이동 | 5는 뒤에서 1번째, 5pop, 4
# 1 2 3 4 5 6 7 : 5가 1번 이동 | 4는 앞에서 0번째, 4pop
# 1 2 3 4 5 6 7 : 4가 0번 이동 |

# 4 2 3 0 2 1 0