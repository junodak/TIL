def seq(N, M, level=0, state=[]):
    if level == M:
        print(*state)
        return

    for i in range(N):
        if any(x >= sample[i] for x in state): continue
        state.append(sample[i])
        seq(N, M, level + 1, state)
        state.pop()

N, M = map(int, input().split())
sample = list(map(int, input("").split()))
sample.sort()
seq(N, M)
