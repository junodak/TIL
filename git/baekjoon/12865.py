def pack(bag, weight, idx=0):
    for i in range(len(bag)):
        if bag[i][0] > weight:


n, k = map(int, input().split())
bag = [[0]*2 for _ in range(n)]

for i in range(n):
    bag[i][0], bag[i][1] = map(int, input().split())

bag.sort()
print(pack(bag))


# print(pack(bag, k))

# 4 7   
# 6 13  0
# 4 8   0
# 3 6   0
# 5 12  0
    
# 7
# 3 6   0
# 4 8   0
# 5 12  0
# 6 13  0
    
# 1. 무게별로 정렬, 무게가 같으면 가치가 큰게 먼저
# 2. 재귀