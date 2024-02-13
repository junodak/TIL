text = input()
stack = []
cnt = 0
for i in range(len(text)):
    if text[i] == '(':
        stack.append(1)
    if text[i] == ')':
        if text[i-1] == '(':
            stack.pop()
            for j in range(len(stack)):
                stack[j] += 1
        else:
            cnt += stack.pop()
print(cnt)