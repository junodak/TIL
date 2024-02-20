def nqueen(line_num, case_cnt):
    for i in range(n):
        if board[line_num][i] == 0:         # Q놓을수있다면
            step = 1                        # 대각 처리용 변수
            for j in range(line_num+1, n):
                board[j][i] += 1            # 가운데줄 추가
                if i-step >= 0:
                    board[j][i-step] += 1   # 왼대각 추가
                if i+step < n:
                    board[j][i+step] += 1   # 오른대각 추가
                step+=1

            if line_num == n-1:             # 마지막 줄이면
                case_cnt += 1
            else:
                case_cnt = nqueen(line_num+1, case_cnt) # 라인 추가해서 재귀
            
            step = 1
            for j in range(line_num+1, n):
                board[j][i] -= 1            # 가운데줄 감소
                if i-step >= 0:
                    board[j][i-step] -= 1   # 왼대각 감소
                if i+step < n:
                    board[j][i+step] -= 1   # 오른대각 감소
                step+=1
    
    return case_cnt  # 경우의수 반환하고 재귀종료
    
n = int(input())
board = [[0]*n for _ in range(n)]
print(nqueen(0, 0))