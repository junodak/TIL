n = int(input())
n_cost = list(map(int, input().split()))
money = int(input())
max_room_num = 0
room_num = 0

# 0은 첫번쨰에 못옴
# 자리수가 많을수록 좋음
# 자리수가 같다면 숫자가 큰게 좋음



for i in range(1,n):
    money -= n_cost[i]
    if money >= 0:
        room_num = room_num*10 + i
    else:
        money += n_cost[i]
        if max_room_num < room_num:
            max_room_num = room_num

print(max_room_num)