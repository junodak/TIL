# # 13
# # 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

# def preorder(T):
#     if T:
#         print(T)
#         preorder(left[T])
#         preorder(right[T])


# N = int(input())    # 정점의 개수 N
# E = N-1             # 간선의 개수는 정점개수 -1
# arr = list(map(int, input().split()))
# left = [0]*(N+1)    # 부모를 인덱스로 왼쪽 자식번호 저장
# right = [0]*(N+1)
# par = [0]*(N+1)     # 자식을 인덱스로 부모 저장

# for i in range(E):
#     p, c = arr[i*2], arr[i*2+1]
#     if left[p]==0:      # 왼쪽 자식이 없으면
#         left[p] = c
#     else:
#         right[p] = c
#     par[c] = p

# c = N
# while par[c] != 0:      # 부모가 있으면
#     c = par[c]          # 부모를 새로운 자식으로 두고
# root = c                # 더이상 부모가 없으면 root
# print(root)
# preorder(root)


def nqueen(line_num, case_cnt):
    if line_num in check:
        if line_num == n-1:             # 마지막 줄이면
            case_cnt += 1
        else:
            case_cnt = nqueen(line_num+1, case_cnt) # 라인 추가해서 재귀
    else:
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
    return case_cnt


n = int(input())
arr = list(map(int, input().split()))
board = [[0]*n for _ in range(n)]
check = []

# 이미 주어진 정보로 board 최신화
for i in range(n):
    if arr[i]:
        check.append(i)
        # board[i][arr[i]] : Q의 위치
        for j in range(n):
            board[i][j] = 1                   # 가로
            board[j][arr[i]-1] = 1            # 세로
            if i+j < n and arr[i]-1+j < n:
                board[i+j][arr[i]-1+j] = 1    # 우하대각
            if i-j >= 0 and arr[i]-1-j >= 0:
                board[i-j][arr[i]-1-j] = 1    # 우상대각
            if i+j < n and arr[i]-1-j >= 0:
                board[i+j][arr[i]-1-j] = 1    # 좌하대각
            if i-j >= 0 and arr[i]-1+j < n:
                board[i-j][arr[i]-1+j] = 1    # 좌상대각

q_case = []
nqueen(0, q_case)
print(*q_case)