N = int(input())
if N == 1:
    print('*')
else:
    star = [['*'] * (4*N-3) for i in range(4*N-1)]

    for i in range(N-1):
        for j in range(4*N-3):
            star[2*N-3-i*2][j] = ' '
            star[2*N+1+i*2][j] = ' '
        for j in range(4*N-1):
            star[j][2*N-3-i*2] = ' '
            star[j][2*N-1+i*2] = ' '
        for j in range(4*N-3):
            star[2*N-4-i*2][j] = '*'
            star[2*N+2+i*2][j] = '*'
        for j in range(4*N-1):
            star[j][2*N-4-i*2] = '*'
            star[j][2*N+i*2] = '*'

    for i in range(N*2-2):
        if star[1+i][4*N-4-i] == '*':
            star[1+i][4*N-4-i] = ' '
        else:
            star[1+i][4*N-4-i] = '*'

    print('*'*(4*N-3))    
    print('*')

    for i in range(2,4*N-1):
        for j in range(4*N-3):
            print(star[i][j],end='')
        print('')
