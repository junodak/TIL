N = int(input())
star = [['*'] * (4*N-3) for i in range(4*N-3)]

for j in range(N-1): 
    for i in range(4*N-3):
        star[2*N-1+j*2][i] = ' '
        star[2*N-3-j*2][i] = ' '
        star[i][2*N-1+j*2] = ' '
        star[i][2*N-3-j*2] = ' '
    for i in range(4*N-3):
        star[2*N+j*2][i] = '*'
        star[2*N-4-j*2][i] = '*'
        star[i][2*N+j*2] = '*'
        star[i][2*N-4-j*2] = '*'

for i in range(4*N-3):
    for j in range(4*N-3):
        print(star[i][j],end='')
    print('')
