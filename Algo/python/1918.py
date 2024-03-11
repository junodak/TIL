txt = input()
stack = []

for i in txt:
    if i.isalpha():
        print(i, end='')
    else:
        stack.append(i)
    
print()