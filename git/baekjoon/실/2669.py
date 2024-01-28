square = [[0]*100 for _ in range(100)]

for i in range(4):
    sq = list(map(int, input().split()))
    for i in range(sq[0], sq[2]):
        for j in range(sq[1], sq[3]):
            square[i][j] = 1

cnt = 0
for i in range(100):
    cnt += square[i].count(1)
print(cnt)