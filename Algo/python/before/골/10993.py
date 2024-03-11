n = int(input())
star = [[' '] * (2**n*2-3) for i in range(2**n-1)]

x = 0
y = 0
for k in range(n,0,-1):
    if n>k:
        x+=2**k
        if k%2 == 1:
            y+=1
        else:
            y+= 2**k-1

    for i in range(2**k-1):
        for j in range(2**k*2-3):
            if i==j and k%2==1:
                star[i+y][2**k-2-j+x] = '*'
                star[i+y][2**k-2+j+x] = '*'
                star[2**k-2+y][j+x] = '*'
                star[2**k-2+y][2**k-2+j+x] = '*'
            if i==j and k%2==0:
                star[i+y][j+x] = '*'
                star[i+y][2**k*2-4-j+x] = '*'
                star[0+y][j+x] = '*'
                star[0+y][2**k-2+j+x] = '*'

for i in range(2**n-1):
    if n%2==1:
        for j in range(2**n*2-3-(2**n-2-i)):
            print(star[i][j],end='')
    if n%2==0:
        for j in range(2**n*2-3-i):
            print(star[i][j],end='')
    print('')