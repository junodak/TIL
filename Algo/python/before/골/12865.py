def pack(items, bag):
    n = len(items)
    dp = [[0] * (bag + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, bag + 1):
            weight, value = items[i - 1]
            if weight > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

    return dp[n][bag]

n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]
print(pack(items, k))

# max_value = 0

# def pack(item, bag, value=0):
#     global max_value
#     for i in range(len(item)):
#         if item[i][0] <= bag:
#             max_value = max(max_value, value+item[i][1])
#             if item[i][0] < bag:
#                 pack(item[i+1:], bag-item[i][0], value+item[i][1])
            
# n, k = map(int, input().split())
# item = [[0]*2 for _ in range(n)]

# for i in range(n):
#     item[i][0], item[i][1] = map(int, input().split())

# item.sort(reverse=True)
# pack(item, k)
# print(max_value)