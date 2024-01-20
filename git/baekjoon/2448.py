n = int(input())

check = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072]
    
def empty(i,j):
    for k in check:
        if (i//k)%2==0 and (j//k)%2:
            return True
    return False

for i in range(n):
    print(' '*(n-i-1),end='')
    for j in range(0,i+1,3):
        if empty(i,j):
            print('      ',end='')
        elif i//3==j/3:
            if i%3==0:
                print('*',' '*(n-i-1),end='')
            elif i%3 ==1:
                print('* *',' '*(n-i-1),end='')
            elif i%3==2:
                print('*****',' '*(n-i-1),end='')
        else:
            if i%3==0:
                print('*     ',end='')
            elif i%3 ==1:
                print('* *   ',end='')
            elif i%3==2:
                print('***** ',end='')
    print('')