def seq(N, M, level=0, state=[]):
    if level == M:
        print(*state)
        return

    for i in range(1, N + 1):
        state.append(i)
        seq(N, M, level + 1, state)
        state.pop()

N, M = map(int, input().split())
seq(N, M)
