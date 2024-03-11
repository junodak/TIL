a, b = map(int, input().split())

count = 1
while (a!=b):
    if b%10 == 1:
        b //= 10
        count += 1
    elif b%2 == 1 or a>b:
        count = -1
        break
    else:
        b //= 2
        count += 1

print(count)