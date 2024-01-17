def seq(N, M, level=0, state=[]):
    if level == M:
        print(*state)
        return

    for i in range(N-level):
        if sample[i-1] == sample[i]: continue
        # if state is None or sample[i] <= state[0]: continue
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


'''
sample : 7 9 9
state : 1 
level : 0

1 7
1 9
7 9
'''
