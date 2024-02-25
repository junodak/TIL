from itertools import product
import sys
from collections import deque
input = sys.stdin.readline
# input = iter(open(0).read().split('\n')).__next__

m, n, o, p, q, r, s, t, u, v, w = map(int, input().split())
arr = [[[[[[[[[[list(map(int, input().split())) for _ in range(n)] for _ in range(o)] for _ in range(p)] for _ in range(q)] for _ in range(r)] for _ in range(s)] for _ in range(t)] for _ in range(u)] for _ in range(v)] for _ in range(w)]

dq = deque()
cnt = 0
for a, b, c, d, e, f, g, h, i, j, k in product(range(w), range(v), range(u), range(t), range(s), range(r), range(q), range(p), range(o), range(n), range(m)):
    if arr[a][b][c][d][e][f][g][h][i][j][k] == 1:
        dq.append((a, b, c, d, e, f, g, h, i, j, k))
    if arr[a][b][c][d][e][f][g][h][i][j][k] == 0:
        cnt += 1

time = 0
while dq:
    a, b, c, d, e, f, g, h, i, j, k = dq.popleft()
    if time < arr[a][b][c][d][e][f][g][h][i][j][k]:
        time = arr[a][b][c][d][e][f][g][h][i][j][k]

    if a-1 >= 0 and arr[a-1][b][c][d][e][f][g][h][i][j][k] == 0:
        dq.append((a-1, b, c, d, e, f, g, h, i, j, k))
        arr[a-1][b][c][d][e][f][g][h][i][j][k] = arr[a][b][c][d][e][f][g][h][i][j][k] + 1
        cnt -= 1
    if a+1 < w and arr[a+1][b][c][d][e][f][g][h][i][j][k] == 0:
        dq.append((a+1, b, c, d, e, f, g, h, i, j, k))
        arr[a+1][b][c][d][e][f][g][h][i][j][k] = arr[a][b][c][d][e][f][g][h][i][j][k] + 1
        cnt -= 1
    
    if b-1 >= 0 and arr[a][b-1][c][d][e][f][g][h][i][j][k] == 0:
        dq.append((a, b-1, c, d, e, f, g, h, i, j, k))
        arr[a][b-1][c][d][e][f][g][h][i][j][k] = arr[a][b][c][d][e][f][g][h][i][j][k] + 1
        cnt -= 1
    if b+1 < v and arr[a][b+1][c][d][e][f][g][h][i][j][k] == 0:
        dq.append((a, b+1, c, d, e, f, g, h, i, j, k))
        arr[a][b+1][c][d][e][f][g][h][i][j][k] = arr[a][b][c][d][e][f][g][h][i][j][k] + 1
        cnt -= 1
    
    if c-1 >= 0 and arr[a][b][c-1][d][e][f][g][h][i][j][k] == 0:
        dq.append((a, b, c-1, d, e, f, g, h, i, j, k))
        arr[a][b][c-1][d][e][f][g][h][i][j][k] = arr[a][b][c][d][e][f][g][h][i][j][k] + 1
        cnt -= 1
    if c+1 < u and arr[a][b][c+1][d][e][f][g][h][i][j][k] == 0:
        dq.append((a, b, c+1, d, e, f, g, h, i, j, k))
        arr[a][b][c+1][d][e][f][g][h][i][j][k] = arr[a][b][c][d][e][f][g][h][i][j][k] + 1
        cnt -= 1
    
    if d-1 >= 0 and arr[a][b][c][d-1][e][f][g][h][i][j][k] == 0:
        dq.append((a, b, c, d-1, e, f, g, h, i, j, k))
        arr[a][b][c][d-1][e][f][g][h][i][j][k] = arr[a][b][c][d][e][f][g][h][i][j][k] + 1
        cnt -= 1
    if d+1 < t and arr[a][b][c][d+1][e][f][g][h][i][j][k] == 0:
        dq.append((a, b, c, d+1, e, f, g, h, i, j, k))
        arr[a][b][c][d+1][e][f][g][h][i][j][k] = arr[a][b][c][d][e][f][g][h][i][j][k] + 1
        cnt -= 1
    
    if e-1 >= 0 and arr[a][b][c][d][e-1][f][g][h][i][j][k] == 0:
        dq.append((a, b, c, d, e-1, f, g, h, i, j, k))
        arr[a][b][c][d][e-1][f][g][h][i][j][k] = arr[a][b][c][d][e][f][g][h][i][j][k] + 1
        cnt -= 1
    if e+1 < s and arr[a][b][c][d][e+1][f][g][h][i][j][k] == 0:
        dq.append((a, b, c, d, e+1, f, g, h, i, j, k))
        arr[a][b][c][d][e+1][f][g][h][i][j][k] = arr[a][b][c][d][e][f][g][h][i][j][k] + 1
        cnt -= 1
    
    if f-1 >= 0 and arr[a][b][c][d][e][f-1][g][h][i][j][k] == 0:
        dq.append((a, b, c, d, e, f-1, g, h, i, j, k))
        arr[a][b][c][d][e][f-1][g][h][i][j][k] = arr[a][b][c][d][e][f][g][h][i][j][k] + 1
        cnt -= 1
    if f+1 < r and arr[a][b][c][d][e][f+1][g][h][i][j][k] == 0:
        dq.append((a, b, c, d, e, f+1, g, h, i, j, k))
        arr[a][b][c][d][e][f+1][g][h][i][j][k] = arr[a][b][c][d][e][f][g][h][i][j][k] + 1
        cnt -= 1
    
    if g-1 >= 0 and arr[a][b][c][d][e][f][g-1][h][i][j][k] == 0:
        dq.append((a, b, c, d, e, f, g-1, h, i, j, k))
        arr[a][b][c][d][e][f][g-1][h][i][j][k] = arr[a][b][c][d][e][f][g][h][i][j][k] + 1
        cnt -= 1
    if g+1 < q and arr[a][b][c][d][e][f][g+1][h][i][j][k] == 0:
        dq.append((a, b, c, d, e, f, g+1, h, i, j, k))
        arr[a][b][c][d][e][f][g+1][h][i][j][k] = arr[a][b][c][d][e][f][g][h][i][j][k] + 1
        cnt -= 1
    
    if h-1 >= 0 and arr[a][b][c][d][e][f][g][h-1][i][j][k] == 0:
        dq.append((a, b, c, d, e, f, g, h-1, i, j, k))
        arr[a][b][c][d][e][f][g][h-1][i][j][k] = arr[a][b][c][d][e][f][g][h][i][j][k] + 1
        cnt -= 1
    if h+1 < p and arr[a][b][c][d][e][f][g][h+1][i][j][k] == 0:
        dq.append((a, b, c, d, e, f, g, h+1, i, j, k))
        arr[a][b][c][d][e][f][g][h+1][i][j][k] = arr[a][b][c][d][e][f][g][h][i][j][k] + 1
        cnt -= 1
    
    if i-1 >= 0 and arr[a][b][c][d][e][f][g][h][i-1][j][k] == 0:
        dq.append((a, b, c, d, e, f, g, h, i-1, j, k))
        arr[a][b][c][d][e][f][g][h][i-1][j][k] = arr[a][b][c][d][e][f][g][h][i][j][k] + 1
        cnt -= 1
    if i+1 < o and arr[a][b][c][d][e][f][g][h][i+1][j][k] == 0:
        dq.append((a, b, c, d, e, f, g, h, i+1, j, k))
        arr[a][b][c][d][e][f][g][h][i+1][j][k] = arr[a][b][c][d][e][f][g][h][i][j][k] + 1
        cnt -= 1
    
    if j-1 >= 0 and arr[a][b][c][d][e][f][g][h][i][j-1][k] == 0:
        dq.append((a, b, c, d, e, f, g, h, i, j-1, k))
        arr[a][b][c][d][e][f][g][h][i][j-1][k] = arr[a][b][c][d][e][f][g][h][i][j][k] + 1
        cnt -= 1
    if j+1 < n and arr[a][b][c][d][e][f][g][h][i][j+1][k] == 0:
        dq.append((a, b, c, d, e, f, g, h, i, j+1, k))
        arr[a][b][c][d][e][f][g][h][i][j+1][k] = arr[a][b][c][d][e][f][g][h][i][j][k] + 1
        cnt -= 1
    
    if k-1 >= 0 and arr[a][b][c][d][e][f][g][h][i][j][k-1] == 0:
        dq.append((a, b, c, d, e, f, g, h, i, j, k-1))
        arr[a][b][c][d][e][f][g][h][i][j][k-1] = arr[a][b][c][d][e][f][g][h][i][j][k] + 1
        cnt -= 1
    if k+1 < m and arr[a][b][c][d][e][f][g][h][i][j][k+1] == 0:
        dq.append((a, b, c, d, e, f, g, h, i, j, k+1))
        arr[a][b][c][d][e][f][g][h][i][j][k+1] = arr[a][b][c][d][e][f][g][h][i][j][k] + 1
        cnt -= 1

    
if cnt:
    print(-1)
else:
    print(time-1)


def solution(open):
    input = iter(open(0).read().split("\n")).__next__
    m, n, o, p, q, r, s, t, u, v, w = list(map(int, input().split()))
    tomatoes = {}
    for W in range(w):
        for V in range(v):
            for U in range(u):
                for T in range(t):
                    for S in range(s):
                        for R in range(r):
                            for Q in range(q):
                                for P in range(p):
                                    for O in range(o):
                                        for N in range(n):
                                            for M, i in zip(range(m), map(int, input().split())):
                                                tomatoes[(M, N, O, P, Q, R, S, T, U, V, W)] = i
    mm, nm, om, pm, qm, rm, sm, tm, um, vm, wm = m-1, n-1, o-1, p-1, q-1, r-1, s-1, t-1, u-1, v-1, w-1
    def side(points, empty):
        sides = set()
        for point in points:
            M, N, O, P, Q, R, S, T, U, V, W = point
            if M < mm: sides.add((M + 1, N, O, P, Q, R, S, T, U, V, W))
            if M > 0:  sides.add((M - 1, N, O, P, Q, R, S, T, U, V, W))
            if N < nm: sides.add((M, N + 1, O, P, Q, R, S, T, U, V, W))
            if N > 0:  sides.add((M, N - 1, O, P, Q, R, S, T, U, V, W))
            if O < om: sides.add((M, N, O + 1, P, Q, R, S, T, U, V, W))
            if O > 0:  sides.add((M, N, O - 1, P, Q, R, S, T, U, V, W))
            if P < pm: sides.add((M, N, O, P + 1, Q, R, S, T, U, V, W))
            if P > 0:  sides.add((M, N, O, P - 1, Q, R, S, T, U, V, W))
            if Q < qm: sides.add((M, N, O, P, Q + 1, R, S, T, U, V, W))
            if Q > 0:  sides.add((M, N, O, P, Q - 1, R, S, T, U, V, W))
            if R < rm: sides.add((M, N, O, P, Q, R + 1, S, T, U, V, W))
            if R > 0:  sides.add((M, N, O, P, Q, R - 1, S, T, U, V, W))
            if S < sm: sides.add((M, N, O, P, Q, R, S + 1, T, U, V, W))
            if S > 0:  sides.add((M, N, O, P, Q, R, S - 1, T, U, V, W))
            if T < tm: sides.add((M, N, O, P, Q, R, S, T + 1, U, V, W))
            if T > 0:  sides.add((M, N, O, P, Q, R, S, T - 1, U, V, W))
            if U < um: sides.add((M, N, O, P, Q, R, S, T, U + 1, V, W))
            if U > 0:  sides.add((M, N, O, P, Q, R, S, T, U - 1, V, W))
            if V < vm: sides.add((M, N, O, P, Q, R, S, T, U, V + 1, W))
            if V > 0:  sides.add((M, N, O, P, Q, R, S, T, U, V - 1, W))
            if W < wm: sides.add((M, N, O, P, Q, R, S, T, U, V, W + 1))
            if W > 0:  sides.add((M, N, O, P, Q, R, S, T, U, V, W - 1))
        return sides & empty
    empty, changed = set(), set()
    tochange = set()
    for key, value in tomatoes.items():
        if value == 1:
            changed.add(key)
            tochange.add(key)
        elif value:
            changed.add(key)
        else:
            empty.add(key)
    # del getside, tomatoes
    for days in range(m*n*o*p*q*r*s*t*u*v*w):
        tochange = side(tochange, empty)
        empty -= tochange
        changed |= tochange
        if not tochange: break
    print(-1 if empty else days)
solution(open)