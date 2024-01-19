n = int(input())

check = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072]

for i in range(n):
    # print(' '*(n-i-1),end='')
    for j in range(0,i+1,3):
        # print(j/3, end='')
        if i%3==0 :
            print('*     ',end='')
        elif i%3 ==1:
            print('* *   ',end='')
        elif i%3==2 :
            print('***** ',end='')
    print('')
