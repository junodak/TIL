import sys
input = sys.stdin.readline
n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
p.append(p[0])
s = 0
for i in range(n):
    s += (p[i][0]*p[i+1][1] - p[i+1][0]*p[i][1])
print(abs(s/2))