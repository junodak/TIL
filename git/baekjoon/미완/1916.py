n = int(input())
m = int(input())
bus = []
for i in range(m):
    bus.append(list(map(int, input().split())))

start, end = map(int, input().split())

cost = 0

for i in range(m):
    if(start == bus[i][0]):
        start2 = (bus[i][1])
        cost += bus[i][2]