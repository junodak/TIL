# # 2467, 2470
# n = int(input())
# arr = list(map(int, input().split()))
# arr.sort(key=lambda x: (abs(x), x))

# min = arr[:2]
# min_num = abs(arr[0] + arr[1])

# for i in range(1, n-1):
#     num = abs(arr[i] + arr[i+1])
#     if min_num > num:
#         min_num = num
#         min = [arr[i], arr[i+1]]

# min.sort()
# print(*min)

# # 14921
# n = int(input())
# arr = list(map(int, input().split()))
# arr.sort(key=lambda x: (abs(x), x))

# min = arr[:2]
# min_num = abs(arr[0] + arr[1])

# for i in range(1, n-1):
#     num = abs(arr[i] + arr[i+1])
#     if min_num > num:
#         min_num = num
#         min = [arr[i], arr[i+1]]

# print(sum(min))


# 2473
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
min = arr[:3]
min_num = arr[0] + arr[1] + arr[2]

for i in range(n-2):
    left, right = i+1, n-1
    while left < right:
        num = arr[i] + arr[left] + arr[right]
        if abs(min_num) > abs(num):
            min = [arr[i], arr[left], arr[right]]
            min_num = num
        if num > 0:
            right -= 1
        elif num < 0:
            left += 1
        else:
            break
    if min_num == 0:
        break
print(*min)