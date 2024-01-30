s = input()
t = input()
s_dic = []
t_dic = []
for i in s:
    s_dic.append(i)
for i in t:
    t_dic.append(i)

while True:
    if s_dic == t_dic:
        print(1)
        break
    elif len(t_dic)==0:
        print(0)
        break
    elif t_dic[-1] == 'A':
        t_dic.pop()
    else:
        t_dic.pop()
        t_dic.reverse()