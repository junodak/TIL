def seq(N, M, level=0, state=[]):
    if level == M:                      # 레벨이 M에 도달하면 출력하고 재귀 종료
        print(*state)
        return

    for i in range(1, N + 1):
        if any(x > i for x in state): continue
        state.append(i)                 # 더 크면 추가
        seq(N, M, level + 1, state)     # 다음 레벨 재귀호출
        state.pop()                     # 현재 레밸 값 제거, 백트레킹

N, M = map(int, input().split())
seq(N, M)
