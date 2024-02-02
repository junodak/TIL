n = int(input())
h = list(map(int, input().split()))
stack = []
idx = []
for i in range(n):
    # 스텍이 비어있지 않고, top보다 현재 높이가 작아질 때까지 pop
    while stack and h[stack[-1]] < h[i]:
        stack.pop()
    if not stack: # 스텍이 비어있으면 왼쪽에 본인보다 큰게 없음
        idx.append(0)
    else: # 본인보다 한단계 큰거의 index 추가
        idx.append(stack[-1] + 1)
    stack.append(i)
print(*idx)




# import sys
# input = sys.stdin.readline

# n = int(input())
# h = list(map(int, input().split()))
# idx = []
# for i in range(n):
#     temp = h[:i]
#     len_temp = i
#     while len_temp and temp.pop() < h[i]:
#         len_temp -= 1
#     idx.append(len_temp)
# print(*idx)


# import sys
# input = sys.stdin.readline

# n = int(input())
# h = list(map(int, input().split()))
# stack = []  # 스택을 사용하여 이전에 본 높이들을 저장할 것입니다.
# idx = []

# for i in range(n):
#     # 스택이 비어 있지 않고 현재 높이가 스택의 top보다 크면,
#     # 스택에서 해당 인덱스를 pop하여 해당 인덱스를 저장합니다.
#     while stack and h[stack[-1]] < h[i]:
#         stack.pop()

#     # 스택이 비어있다면 현재 인덱스까지의 가장 큰 높이는 0입니다.
#     if not stack:
#         idx.append(0)
#     # 아니면 스택의 top에 있는 인덱스가 현재 인덱스까지의 가장 큰 높이입니다.
#     else:
#         idx.append(stack[-1] + 1)

#     # 현재 인덱스를 스택에 추가합니다.
#     stack.append(i)

# print(*idx)