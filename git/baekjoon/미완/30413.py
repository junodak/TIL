m = 10**9+7
a, b = map(int, input().split())
if a==1:
    print(b)
else:
    print(((pow(a,b,m)-1)%m)*(pow(a-1,m-2,m))%m)
# print(((pow(a,b)-1)//(a-1)) % m)
