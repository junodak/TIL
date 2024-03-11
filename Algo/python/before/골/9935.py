string = input()
exp = input()

stack = []

for char in string:
    stack.append(char)
    if len(stack) >= len(exp) and ''.join(stack[-len(exp):]) == exp:
        for _ in range(len(exp)):
            stack.pop()

result = ''.join(stack)

if result == '':
    print('FRULA')
else:
    print(result)


# import re

# string = input()
# exp = input()
# string_temp = ''

# while string != string_temp:
#     string_temp = string
#     string = re.sub(exp, '', string)

# if string == '':
#     print('FRULA')
# else:
#     print(string)


# string = input()
# exp = input()
# string_temp = ''

# while string != string_temp:
#     string_temp = string
#     string = string.replace(exp,'')
# if string =='':
#     print('FRULA')
# else:
#     print(string)