import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    q = []
    plus = k//2                                         # 아무리 많이 확산되어도 k//2만큼임
    arr = [[0]*(m+plus*2) for _ in range(n+plus*2)]     # k//2만큼 0 껍데기 씌우기
    for i in range(plus, plus+n):
        arr[i][plus:plus+m] = list(map(int, input().split()))
        for j in range(plus, plus+m):
            if arr[i][j]:                               # 입력받으면서 줄기세포들 q에 append
                q.append((arr[i][j], i, j, 0))          # append(시간, i좌표, j좌표, 활성화여부)
    q.sort(reverse=True)                                # 생명력수치가 더 높은걸 먼저해야함
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while k:                                            # k 사이클
        for _ in range(len(q)):                         # 1 사이클은 q에 들어있는 만큼
            time, x, y, active = q.pop(0)
            if active:                                  # 활성화 상태일때
                if time == arr[x][y]:                   # 활성화 된지 1시간 되었다면
                    for i in range(4):                  # 확산
                        di, dj = x + d[i][0], y + d[i][1]
                        if 0 <= di < n+plus*2 and 0 <= dj < m+plus*2:
                            if arr[di][dj] == 0:
                                arr[di][dj] = arr[x][y]
                                q.append((arr[di][dj], di, dj, 0))  # 확산할때 활성화상태 0으로
                if time > 1:
                    q.append((time-1, x, y, active))    # 1보다 크면 시간 줄여서 다시 append
                else:
                    arr[x][y] = -1                      # 1이 되면 죽은상태(-1)로 변경
            else:
                if time > 1:
                    q.append((time-1, x, y, active))
                else:
                    q.append((arr[x][y], x, y, 1))      # 1이 되면 활성화 시켜서 다시 append

        k -= 1                                          # 사이클 감소
    print(f'#{tc} {len(q)}')                            # 다 끝나고 q에 남아 있는 개수 = 활성화+비활성화 개수
