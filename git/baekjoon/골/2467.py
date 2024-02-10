n = int(input())
arr = list(map(int, input().split()))
arr.sort(key=lambda x: (abs(x), x))

min = arr[:2]
min_num = abs(arr[0] + arr[1])

for i in range(1, n-1):
    num = abs(arr[i] + arr[i+1])
    if min_num > num:
        min_num = num
        min = [arr[i], arr[i+1]]

min.sort()
print(*min)




# for _ in range(n-1):  # 총 n-1번 이동
#     # left가 음수, right가 양수 라면
#     if arr[left] < 0 and arr[right] > 0:
#         if min_num > abs(arr[left] + arr[right]):

    

#     if :
#         left += 1
#     else:
#         right -= 1