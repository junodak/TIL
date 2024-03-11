n = int(input())
voca = []
for i in range(n):
    voca.append(input())

voca = list(set(voca))
voca.sort(key=lambda x: (len(x),x))

for i in voca:
    print(i)