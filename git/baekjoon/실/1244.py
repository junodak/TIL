n = int(input())
switch = list(map(int, input().split()))

stdnt_num = int(input())
for i in range(stdnt_num):
    gender, num = map(int, input().split())
    if gender == 1:
        for j in range(num-1, n, num):
            switch[j] = int(not switch[j])
    elif gender == 2:
        switch[num-1] = int(not switch[num-1])
        for j in range(1,n):
            if (num-1-j)<0 or (num-1+j)>=n:
                break
            elif switch[num-1-j] == switch[num-1+j]:
                switch[num-1-j] = int(not switch[num-1-j])
                switch[num-1+j] = int(not switch[num-1+j])
            else:
                break

for i in range(n):
    print(switch[i], end=' ')
    if i%20 == 19:
        print()