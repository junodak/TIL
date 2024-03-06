from collections import deque

# 상하좌우 델타
dt = [(-1, 0), (1, 0), (0, -1), (0, 1)]

tc = int(input())
for _ in range(tc):

    # height, width 입력
    hi, wi = map(int, input().split())

    # arr 입력, 껍데기 씌우기
    arr = [['.']*(wi+2) for _ in range(hi+2)]
    for i in range(1, hi+1):
        arr[i][1:wi+1] = list(input())

    # key 입력, 0이면 빈거로
    ky = input()

    # '$'의 개수를 세는 cnt, 소문자를 찾았는지 여부를 확인하는 check
    cnt = 0
    check = True

    # 소문자를 못찾았으면 종료
    while check:
        check = False

        # visited, que 생성
        visited = [[0]*(wi+2) for _ in range(hi+2)]
        que = deque()

        # 시작은 (0, 0), '$'의 개수도 0
        que.append((0, 0))
        visited[0][0] = 1
        cnt = 0

        # BFS
        while que:
            di, dj = que.popleft()

            # 델타 4방향 탐색
            for dtx, dty in dt:
                dx = di + dtx
                dy = dj + dty

                # 범위내에 있고, 가본적 없고, '*'이 아니면
                if 0 <= dx < hi+2 and 0 <= dy < wi+2 and visited[dx][dy] == 0 and arr[dx][dy] != '*':

                    # '.', '$', 대문자, 소문자인 경우 각각 처리
                    if arr[dx][dy] == '.':
                        que.append((dx, dy))
                    elif arr[dx][dy] == '$':
                        que.append((dx, dy))
                        cnt += 1
                    elif arr[dx][dy].isupper():
                        if arr[dx][dy].lower() in ky:
                            que.append((dx, dy))
                    elif arr[dx][dy].islower():
                        que.append((dx, dy))
                        ky += arr[dx][dy]
                        arr[dx][dy] = '.'
                        check = True

                    # 방문처리
                    visited[dx][dy] = 1
    print(cnt)