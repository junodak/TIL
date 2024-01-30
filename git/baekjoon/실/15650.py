def seq(N, M, level=0, state=[]):
    if level == M:
        print(*state)
        return

    for i in range(1, N + 1):
        if any(x >= i for x in state): continue
        state.append(i)
        seq(N, M, level + 1, state)
        state.pop()

N, M = map(int, input().split())
seq(N, M)
