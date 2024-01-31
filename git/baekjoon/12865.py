max_value = 0

def pack(item, bag, value=0):
    global max_value
    for i in range(len(item)):
        if item[i][0] <= bag:
            max_value = max(max_value, value+item[i][1])
            if item[i][0] < bag:
                pack(item[i+1:], bag-item[i][0], value+item[i][1])
            
n, k = map(int, input().split())
item = [[0]*2 for _ in range(n)]

for i in range(n):
    item[i][0], item[i][1] = map(int, input().split())

item.sort(reverse=True)
pack(item, k)
print(max_value)

# 5 10
# 4 10
# 3 20
# 2 6
# 1 5