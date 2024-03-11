n = int(input())
weight = [0]*n
for i in range(n):
    weight[i] = int(input())

weight.sort()

for i in range(n):
    weight[i] *= (n-i)

print(max(weight))