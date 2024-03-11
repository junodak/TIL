import sys
input = sys.stdin.readline

n = int(input())
arr = []
pop_idx = 0

for _ in range(n):
    order = input().split()
    if order[0] == 'push':
        arr.append(int(order[1]))
    elif order[0] == 'pop':
        if len(arr) - pop_idx > 0:
            print(arr[pop_idx])
            pop_idx += 1
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(arr) - pop_idx)
    elif order[0] == 'empty':
        if len(arr) - pop_idx > 0:
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if len(arr) - pop_idx > 0:
            print(arr[pop_idx])
        else:
            print(-1)
    elif order[0] == 'back':
        if len(arr) - pop_idx > 0:
            print(arr[-1])
        else:
            print(-1)


# import queue
# import sys
# input = sys.stdin.readline

# n = int(input())
# q = queue.Queue()
# q_front, q_back = -1, -1

# for _ in range(n):
#     order = input().split()
#     if order[0] == 'push':
#         q.put(int(order[1]))
#         q_back = int(order[1])
#         if q.qsize()==1:
#             q_front = int(order[1])
#     elif order[0] == 'pop':
#         try:
#             print(q.get(False))
#             try:
#                 q_front = q.get(False)
#                 q.put(q_front)
#             except:
#                 q_front = -1
#         except:
#             q_front = -1
#             q_back = -1
#             print(-1)
#     elif order[0] == 'size':
#         print(q.qsize())
#     elif order[0] == 'empty':
#         print(int(q.empty()))
#     elif order[0] == 'front':
#         print(q_front)
#     elif order[0] == 'back':
#         print(q_back)