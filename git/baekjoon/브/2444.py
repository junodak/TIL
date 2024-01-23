N = int(input())
for i in range(1,N+1):
    print(' '*(N-i), end='')
    print('*'*(i*2-1))

for i in range(N-1,0,-1):
    print(' '*(N-i), end='')
    print('*'*(i*2-1))
