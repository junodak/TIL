def seq(N, M, level=0, state=[]):
    if level == M:
        print(*state)
        return

    for i in range(N-level):
        if i!=0 and sample[i] == sample[i-1]: continue
        state.append(sample[i])
        sample.pop(i)
        seq(N, M, level + 1, state)
        sample.append(state[level])
        sample.sort()
        state.pop()

N, M = map(int, input().split())
sample = list(map(int, input("").split()))
sample.sort()
seq(N, M)
