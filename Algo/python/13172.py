def jun_pow(base, exp, mod):
    res = 1
    while exp:
        if exp % 2:
            res = (res*base) % mod
        base = (base*base) % mod
        exp >>= 1
    return res

import sys
input = sys.stdin.readline
mod = 10**9+7
res = 0
for i in range(int(input())):
    n, s = map(int, input().split())
    res += (s*jun_pow(n, -1, mod) % mod)
print(res % mod)