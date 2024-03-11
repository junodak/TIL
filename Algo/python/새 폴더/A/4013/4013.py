import sys
sys.stdin = open('input.txt')


def rotate(num, rot):
    # 자석끼리 다른극으로 붙어있는지 확인
    point = []
    for i in range(3):
        if mag[i][2] != mag[i+1][6]:
            point.append((i, i+1))

    # 자석들 어떤 방향으로 돌려야 하는지 확인 (BFS)
    turn = [0, 0, 0, 0]
    turn[num] = rot
    q = [(num, rot)]
    while q:
        x, y = q.pop(0)
        if x-1 >= 0 and turn[x-1] == 0 and (x-1, x) in point:
            turn[x-1] = -y
            q.append((x-1, -y))
        if x+1 < n and turn[x+1] == 0 and (x, x+1) in point:
            turn[x+1] = -y
            q.append((x+1, -y))

    # 자석들 방향에 맞게 돌리면서 점수 계산
    score = 0
    for i in range(4):
        if turn[i] == 1:
            temp = [mag[i][7]]
            temp.extend(mag[i][0:7])
            mag[i] = temp[:]
            if mag[i][0] == 1:
                score += 2**i
        elif turn[i] == -1:
            temp = mag[i][1:8]
            temp.append(mag[i][0])
            mag[i] = temp[:]
            if mag[i][0] == 1:
                score += 2**i
    return score


T = int(input())
for tc in range(1, T+1):
    k = int(input())
    mag = [list(map(int, input().split())) for _ in range(4)]

    total_score = 0
    for _ in range(k):
        n, r = map(int, input().split())
        total_score += rotate(n-1, r)
    print(f'#{tc} {total_score}')
