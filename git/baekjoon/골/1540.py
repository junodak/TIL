import math

def cal(n):
    # n보다 작은 제곱수 구하기
    root = int(math.sqrt(n)) 
    num_of_square = pow(root,2)

    # 제곱수의 정사각형 개수 구하기
    square_count = 0
    for i in range(root):
        square_count += pow(i,2)
    
    # 점이 N개일때 정사각형 개수 추가로 구하기
    count = 0
    for i in range(n - num_of_square):
        square_count += count
        count += 1
        if count == root:
            count = 0

    return square_count

n = int(input())
if n<4:
    print(0)
else:
    print(cal(n))


# 04 : 1
# -----------
# 05 : 1 (+0)
# 06 : 2 (+1)

# 07 : 2 (+0)
# 08 : 3 (+1)
# 09 : 5 (+2)
# -----------
# 10 : 5 (+0)
# 11 : 6 (+1)
# 12 : 8 (+2)

# 13 : 8 (+0)
# 14 : 9 (+1)
# 15 : 11 (+2)
# 16 : 14 (+3)
# -----------
# 17 : 14 (+0)
# 18 : 15 (+1)
# 19 : 17 (+2)
# 20 : 20 (+3)

# 21 : 20 (+0)
# 22 : 21 (+1)
# 23 : 23 (+2)
# 24 : 26 (+3)
# 25 : 30 (+4)
# -----------