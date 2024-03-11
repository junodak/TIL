n, s = map(int, input().split())
a = list(map(int, input().split()))
L, R = 0, 0
p = a[L]
length = n+1

while R < n:
    if p <= s:
        if p == s:
            length = min(length, R-L+1)
        R += 1
        if R >= n:
            break
        p += a[R]
    if p >= s:
        length = min(length, R-L+1)
        p -= a[L]
        L += 1

if length == n+1:
    print(0)
else:
    print(length)
