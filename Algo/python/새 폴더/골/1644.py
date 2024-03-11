def primes(n):
    arr = [0,0] + [1]*(n-1)
    lst = [0]

    for i in range(2, int(n ** 0.5) + 1):
        if arr[i]:
            for j in range(i*i, n+1, i):
                arr[j] = 0
    
    for i in range(n+1):
        if arr[i]:
            lst.append(lst[-1]+i)

    return lst

n = int(input())
arr = primes(n)


left = 0
cnt = 0
for right in range(1, len(arr)):
    if arr[right] - arr[left] < n:
        pass
    elif arr[right] - arr[left] == n:
        cnt += 1
        pass
    else:
        while True:
            left += 1
            if arr[right] - arr[left] > n:
                pass
            elif arr[right] - arr[left] == n:
                cnt += 1
                break
            else:
                break
print(cnt)