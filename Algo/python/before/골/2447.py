
N = int(input())
star = [['*'] * N for i in range(N)]
square = [1,3,9,27,81,243,729,2187]

for k in square:
    for i in range(N):
        for j in range(N):
            if (int(i/k))%3 == 1 and int((j/k))%3 ==1:
                star[i][j] = ' '
    if N == (square): break

for i in range(N):
    for j in range(N):
        print(star[i][j],end='')
    print('')
