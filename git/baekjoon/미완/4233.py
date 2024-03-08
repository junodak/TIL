while True:
    p, a = map(int, input().split())
    if p == 0 and a == 0:
        break
    if pow(a, p, p) == a:
        

        print('yes')
    else:
        print('no')