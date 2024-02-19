def seq(n, s, sum=0, cnt=0, idx = 0):
    for i in range(idx, n):
        if sum+arr[i] <= s:     # 더한게 s보다 작다면 계속 더해
            if sum+arr[i] == s: # s랑 같으면 카운트 올려줘
                cnt +=1
            cnt = seq(n, s, sum+arr[i], cnt, i+1)
        else:
            return cnt
    return cnt

n, s = map(int, input().split())
arr = list(map(int, input().split()))
if s < 0: # s가 음수면 전부 부호 뒤집기
    s *= -1
    for i in range(n):
        arr[i] *= -1
arr.sort()
print(seq(n, s))