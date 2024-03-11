n = int(input())
m = list(map(int, input().split()))

two = m[0]+m[1]
for i in range(6):
    for j in range(i+1,6):
        if i+j != 5:
            two = min(two,m[i]+m[j])
tre = min(m[0],m[5])+min(m[1],m[4])+min(m[2],m[3])

if n==1:
    print(sum(m)-max(m))
else:
    a = 4
    b = 8*n-12
    c = (5*n-6)*(n-2)
    print(a*tre+b*two+c*min(m))