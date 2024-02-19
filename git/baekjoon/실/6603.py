def seq(N, M, level=0, state=[]):  # N과M(6)와 동일
    if level == M:
        print(*state)
        return

    for i in range(N):
        if any(x >= arr[i] for x in state): continue
        state.append(arr[i])
        seq(N, M, level + 1, state)
        state.pop()

txt = input()
while txt != '0':
    arr = list(map(int, txt.split()))
    seq(arr.pop(0), 6)
    print()
    txt = input()