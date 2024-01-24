# string = input()
# exp = input()
# if len(exp)==1:
#     string = string.replace(exp,'')
#     if string =='':
#         print('FRULA')
#     else:
#         print(string)
# else:
#     while string != string.replace(exp,''):
#         string = string.replace(exp,'')
#     if string =='':
#         print('FRULA')
#     else:
#         print(string)


string = input()
exp = input()
string_temp = ''

while string != string_temp:
    string_temp = string
    string = string.replace(exp,'')
if string =='':
    print('FRULA')
else:
    print(string)