import copy

def button(i, j):
    copy_arr[i][j] += 1
    copy_arr[i][j] %= 2
    if i-1 >= 0:
        copy_arr[i-1][j] += 1
        copy_arr[i-1][j] %= 2
    if i+1 < 10:
        copy_arr[i+1][j] += 1
        copy_arr[i+1][j] %= 2
    if j-1 >= 0:
        copy_arr[i][j-1] += 1
        copy_arr[i][j-1] %= 2
    if j+1 < 10:
        copy_arr[i][j+1] += 1
        copy_arr[i][j+1] %= 2

txt = [input() for _ in range(10)]
arr = [[0]*10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        if txt[i][j] == 'O':
            arr[i][j] = 1

min_cnt = 101
for x in range(2**10):
    copy_arr = copy.deepcopy(arr)
    cnt = 0
    
    d_to_b = list(map(int, f'{x:010b}'))
    for i in range(10):
        if d_to_b[i]:
            button(0, i)
            cnt += 1

    for i in range(1, 10):
        for j in range(10):
            if copy_arr[i-1][j]:     # 위에꺼가 1이면 누르기
                button(i, j)
                cnt += 1

    if sum(copy_arr[9]) == 0:
        min_cnt = min(min_cnt, cnt)

if min_cnt == 101:
    min_cnt = -1
print(min_cnt)