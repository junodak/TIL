n = int(input())
if n==0:
    print(0)
    print(0)
elif n>0:
    arr = [0,1,1]
    for i in range(n-1):
        arr[2] = (arr[0] + arr[1]) % 1000000000
        arr[0] = arr[1]
        arr[1] = arr[2]
    print(1)
    print(arr[1])
else:
    arr = [1,0,1]
    for i in range(1-n):
        if arr[0] - arr[1] > 0:
            arr[2] = (arr[0] - arr[1]) % 1000000000
        else:
            arr[2] = (arr[0] - arr[1]) % 1000000000 - 1000000000
        arr[0] = arr[1]
        arr[1] = arr[2]
    if arr[0]>0:
        print(1)
        print(arr[0])
    else:
        print(-1)
        print(-arr[0])

# if n == 0:
#     print(0)
#     print(0)
# elif n > 0:
#     arr = [0, 1] + [0]*(n-1)
#     for i in range(n-1):
#         arr[i+2] = arr[i+1] + arr[i]
#     print(1)
#     print(arr[n] % 1000000000)
# else:
#     arr = [1, 0] + [0]*(-n)
#     for i in range(-n):
#         arr[i+2] = arr[i] - arr[i+1]
#     if abs(arr[-n+1]) < 0:
#         print(-1)
#     else:
#         print(1)
#     print(abs(arr[-n+1]) % 1000000000)