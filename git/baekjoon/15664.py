def seq(N, M, level=0, state=[], check = 0):
    if level == M:
        print(*state)
        return

    for i in range(check, N-level):
        if i==0 or sample[i-1] != sample[i]:
            state.append(sample[i])
            sample.pop(i)
            seq(N, M, level + 1, state, i)
            sample.append(state[level])
            sample.sort()
            state.pop()

N, M = map(int, input().split())
sample = list(map(int, input("").split()))
sample.sort()
seq(N, M)
