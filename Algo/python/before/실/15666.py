def seq(N, M, level=0, state=[], check = 0):
    if level == M:
        print(*state)
        return

    for i in range(check, N):
        state.append(sample[i])
        seq(N, M, level + 1, state, i)
        state.pop()

N, M = map(int, input().split())
sample = list(map(int, input("").split()))
sample = list(set(sample))
sample.sort()
seq(len(sample), M)
