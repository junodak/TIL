text = input()
stack = []
for i in text:
    stack.append(i)
    if len(stack) >= 2:
        if stack[-1] == ')' and stack[-2] == '(' or stack[-1] == ']' and stack[-2] == '[':
            stack.pop()
            stack.pop()

result = '0'
for i in range(len(text)):
    if text[i] == '(' or text[i] == '[':
        if text[i-1] == ')' or text[i-1] == ']':
            result += '+'   # )(, ](, )[, ][ 꼴이면 사이에 + 추가
        result += '('       # ( -> (, [ -> (
    else:
        if text[i-1] == '(' or text[i-1] == '[':
            result += '1'   # (), [] 꼴이면 사이에 1 추가
        if text[i] == ')':
            result += ')*2' # ) -> )*2
        else:
            result += ')*3' # ] -> )*3

if len(stack):              # 가능한 연산이 아니면 0출력
    print(0)
else:
    print(eval(result))     # 가능한 연산이라면 result계산