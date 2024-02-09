arr = '(((()(()()))(())()))(()())'
d, cnt = 0, 0
for i in arr:
    if i == '(':
        d += 1
    else:
        d -= 1
        cnt += d
print(cnt)