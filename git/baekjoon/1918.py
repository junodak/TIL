# txt = input()
# stack = []

# for i in txt:
#     if i.isalpha():
#         print(i, end='')
#     else:
#         stack.append(i)
    
# print()


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    if '1'*n == bin(m)[-n:]:
        txt = 'ON'
    else:
        txt = 'OFF'
    print(f'#{tc} {txt}')