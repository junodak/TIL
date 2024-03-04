# n, m = map(int, input().split())
# city = [0]*n
# for i in range(n):
#     city[i] = list(map(int, input().split()))
n, m = 5, 3
city = [
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 2, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1]    
    # [0, 2, 0, 1, 0],
    # [1, 0, 1, 0, 0],
    # [0, 0, 0, 0, 0],
    # [2, 0, 0, 1, 1],
    # [2, 2, 0, 1, 2]
    # [0, 0, 1, 0, 0],
    # [0, 0, 2, 0, 1],
    # [0, 1, 2, 0, 0],
    # [0, 0, 1, 0, 0],
    # [0, 0, 0, 0, 2]
    ]

def cal_dis(city, n):
    chic_dis = 0
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                chic_dis += search(city, i, j, n)
    return chic_dis

def search(city, i, j, n):
    min_distance = 50
    for x in range(n):
        for y in range(n):
            if city[x][y] == 2:
                distance = abs(i - x) + abs(j - y)
                min_distance = min(min_distance, distance)
    return min_distance

print(cal_dis(city, n))


# 각 집에서 치킨집까지 거리를 리스트로 해두고, 없애야 하는 치킨집을 골라야함.