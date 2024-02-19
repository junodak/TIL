def seq(n, s, sum=0, cnt=0, idx = 0):
    for i in range(idx, n):
        if sum+arr[i] < s: # s보다 작다면 더 더해
            cnt = seq(n, s, sum+arr[i], cnt, i+1)
        elif sum+arr[i] == s:  # 다 더한값이 s와 같다면
            return cnt + 1
        else:
            return cnt

n, s = map(int, input().split())
arr = list(map(int, input().split()))
print(seq(n, s))