# 13545번

def seq(N, M, level, state, query, cache):
    if level == M:
        total_sum = 0
        for i in range(M):
            total_sum += query[i]
            if total_sum == 0:
                return True
        return False

    if (level, tuple(state)) in cache:
        return cache[(level, tuple(state))]

    for i in range(N):
        if any(x >= i for x in state):
            continue
        state.append(i)
        if seq(N, M, level + 1, state, query, cache):
            cache[(level, tuple(state))] = True
            return True
        state.pop()

    cache[(level, tuple(state))] = False
    return False

n = int(input())
a = list(map(int, input().split()))
m = int(input())
i = [0] * m
j = [0] * m
query_list = []

for x in range(m):
    i[x], j[x] = map(int, input().split())
    query_list.append(a[i[x] - 1:j[x]])

for x in range(m):
    cache = {}  # 메모이제이션 캐시 초기화
    for y in range(len(query_list[x]), 0, -1):
        if seq(len(query_list[x]), y, 0, [], query_list[x], cache):
            print(y)
            break
    else:
        print(0)


# def seq(N, M, level=0, state=[]):
#     if level == M:
#         sum = 0
#         for i in range(M):
#             sum += query[x][state[i]]
#             if sum == 0:
#                 global check
#                 check = True
#         return

#     for i in range(N):
#         if any(x >= i for x in state): continue
#         state.append(i)
#         seq(N, M, level + 1, state)
#         state.pop()

# n = int(input())
# a = list(map(int,input().split()))
# m = int(input())
# i = [0]*m
# j = [0]*m
# query = [0]*m
# len_q = [0]*m

# for x in range(m):
#     i[x],j[x] = map(int,input().split())
#     query[x] = a[i[x]-1:j[x]]
#     len_q[x] = j[x] - i[x] + 1

# for x in range(m):
#     for y in range(len_q[x]-1,-1,-1):
#         check = False
#         seq(len_q[x], y+1)
#         if check == True:
#             print(y+1)
#             break
#     if check == False:
#         print(0)