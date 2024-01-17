def seq(N, M, level=0, state=[]):
    if level == M:
        print(*state)
        return

    for i in range(N):
        state.append(sample[i])
        seq(N, M, level + 1, state)
        state.pop()

N, M = map(int, input().split())
sample = list(map(int, input("").split()))
sample.sort()
seq(N, M)
