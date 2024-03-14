n = int(input())
arr = [0]*10

len_n = len(str(n))-1
n_0 = int(str(n)[0])
start_n = n_0 * 10**len_n - 1

arr[0] = int(str(len_n-2)+'8'*(len_n-2)+'9')
for i in range(1, 10):
    arr[i] = len_n * 10**(len_n-1)

temp = arr[1]
for i in range(10):
    arr[i] += (n_0-1)*temp
for i in range(1, n_0):
    arr[i] += 10**len_n

for i in range(start_n + 1, n+1):
    for j in str(i):
        arr[int(j)] += 1
print(*arr)