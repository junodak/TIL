# n, m = map(int, input().split())
# city = [0]*n
# for i in range(n):
#     city[i] = list(map(int, input().split()))
n, m = 5, 3
city = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2]
    ]

def cal_dis(city, n):
    chic_dis = 0
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                chic_dis += search(city, i, j, n)
    return chic_dis

def search(city, i, j, n):
    pass

cal_dis(city, n)