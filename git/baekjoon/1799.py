def bishop(cnt, y):
    global max_cnt
    for i in range(y, n):
        for j in range(n):
            if chess_map[i][j] == 0: # 비숍 놓을 수 있다면

                cnt += 1
                # 비숍 놓고 경로 카운팅
                for k in range(n):
                    if i+k < n and j+k < n:
                        chess_map[i+k][j+k] += 1
                    if i-k >= 0 and j-k >= 0:
                        chess_map[i-k][j-k] += 1
                    if i-k >= 0 and j+k < n:
                        chess_map[i-k][j+k] += 1
                    if i+k < n and j-k >= 0:
                        chess_map[i+k][j-k] += 1

                # 다음 비숍 놓으러 갑니다
                # 대신 i줄 부터 탐색시작
                bishop(cnt, i)

                # 놓고 돌아오면 카운팅 제거
                cnt -= 1
                for k in range(n):
                    if i+k < n and j+k < n:
                        chess_map[i+k][j+k] -= 1
                    if i-k >= 0 and j-k >= 0:
                        chess_map[i-k][j-k] -= 1
                    if i-k >= 0 and j+k < n:
                        chess_map[i-k][j+k] -= 1
                    if i+k < n and j-k >= 0:
                        chess_map[i+k][j-k] -= 1
    
    # 여기까지 왔다는건 더할게 없다는거
    max_cnt = max(cnt, max_cnt)
    return cnt

n = int(input())
chess_map = [list(map(int, input().split())) for _ in range(n)]

# 편의를 위해 1과 0을 바꾸기
for i in range(n):
    for j in range(n):
        if chess_map[i][j]:
            chess_map[i][j] = 0
        else:
            chess_map[i][j] = 1
max_cnt = 0
# cnt는 0, 시작줄은 0
cnt = bishop(0, 0)
print(max_cnt)