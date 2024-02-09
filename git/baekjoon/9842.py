def primes(m, n):
    arr = [0, 0] + [1]*(n-1)
    for i in range(2, int(n ** 0.5) + 1):
        if arr[i]:
            for j in range(i*i, n+1, i):
                arr[j] = 0
    cnt = 0
    for i in range(m, n+1):
        if arr[i]:
            cnt += 1
    return cnt
while True:
    try:
        m, n = map(int, input().split())
        print(primes(m, n))
        print()
        a = input()
        if a != '':
            break
    except:
        break