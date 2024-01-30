import heapq

n = int(input())
meetings = []

for i in range(n):
    s, t = map(int, input().split())
    meetings.append((s, t))

meetings.sort(key=lambda x: (x[0], x[1]))

room = []  # 수업이 끝나는 시간을 저장하는 리스트

for meeting in meetings:
    start_time, end_time = meeting

    if not room or room[0] > start_time:
        # 새로운 강의실이 필요한 경우
        heapq.heappush(room, end_time)
    else:
        # 기존 강의실을 이용하는 경우
        heapq.heappop(room)
        heapq.heappush(room, end_time)

print(len(room))


# 힙 안쓰다가 시간초과 낭패

# n = int(input())
# meetings = []

# for i in range(n):
#     s, t = map(int, input().split())
#     meetings.append((s, t))

# meetings.sort(key=lambda x: (x[0], x[1]))

# room = [meetings[0][1]]
# for i in range(1,n):
#     check = True
#     for j in range(len(room)):
#         if meetings[i][0] >= room[j]:
#             room[j] = meetings[i][1]
#             check = False
#             break
#     if check:
#         room.append(meetings[i][1])

# print(len(room))