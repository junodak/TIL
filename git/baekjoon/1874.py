# n = int(input())
# arr = []
# for _ in range(n):
#     arr.append(int(input()))
# num = list(range(1,n+1))

n = 8
arr = [1,2,5,3,4]
# arr = [4,3,6,8,7,5,2,1]

num = 1
stack = []
text = []

for i in arr:
    while i>=num or i in stack:
        if i >= num:
            stack.append(num)
            num+=1
            text.append('+')
        if i == stack[-1]:
            stack.pop()
            text.append('-')
print(arr)