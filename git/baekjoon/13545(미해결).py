# 13545번

def seq(N, M, level=0, state=[]):
    if level == M:
        sum = 0
        for i in range(M):
            sum += query[x][state[i]]
            if sum == 0:
                global check
                check = True
        return

    for i in range(N):
        if any(x >= i for x in state): continue
        state.append(i)
        seq(N, M, level + 1, state)
        state.pop()

n = int(input())
a = list(map(int,input().split()))
m = int(input())
i = [0]*m
j = [0]*m
query = [0]*m
len_q = [0]*m

for x in range(m):
    i[x],j[x] = map(int,input().split())
    query[x] = a[i[x]-1:j[x]]
    len_q[x] = j[x] - i[x] + 1

for x in range(m):
    for y in range(len_q[x]-1,-1,-1):
        check = False
        seq(len_q[x], y+1)
        if check == True:
            print(y+1)
            break
    if check == False:
        print(0)