
# n = 5
# arr = [1,2,5,3,4]
# n = 8
# arr = [4,3,6,8,7,5,2,1]

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

num = 1
stack = []
text = []

for i in arr:
    while i>=num or i in stack:
        if i >= num:
            stack.append(num)
            num+=1
            text.append('+')
        elif i == stack[-1]:
            stack.pop()
            text.append('-')
        else:
            break

if len(stack):
    print('NO')
else:
    for i in text:
        print(i)