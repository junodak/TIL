# 14501번

max_money = 0

def benefit(day=0, money=0):
    global max_money
    for i in range(day,N):
        money += p[i]
        max_money = max(max_money,money)
        if i+t[i] >= N:
            money -= p[i]
            continue
        else:
            benefit(i+t[i], money)
        money -= p[i]
    return max_money

N = int(input())
t = [0]*(N+1)
p = [0]*(N+1)

for i in range(N):
    t[i], p[i] = map(int,input().split())
    if t[i] > (N-i):
        p[i] = 0

print(benefit())








