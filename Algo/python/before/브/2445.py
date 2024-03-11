N = int(input())
for i in range(N):
    print('*'*(i+1), end='')
    print(' '*((N-i-1)*2), end='')
    print('*'*(i+1))
for i in range(N-2,-1,-1):
    print('*'*(i+1), end='')
    print(' '*((N-i-1)*2), end='')
    print('*'*(i+1))
