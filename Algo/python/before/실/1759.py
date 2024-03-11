def seq(N, M, level=0, state=[]):  # N과M(6)와 동일
    if level == M:
        v_cnt, c_cnt = 0, 0 # 모음자음 개수
        for i in state:
            if i in vowel:
                v_cnt += 1
            else:
                c_cnt += 1
        if v_cnt >= 1 and c_cnt >= 2:                
            for i in state:
                print(i, end='')
            print()
        return

    for i in range(N):
        if any(x >= arr[i] for x in state): continue
        state.append(arr[i])
        seq(N, M, level + 1, state)
        state.pop()

l, c = map(int, input().split())
arr = list(input().split())
arr.sort()
vowel = ['a', 'e', 'i', 'o', 'u']  # 모음표본
seq(c, l)