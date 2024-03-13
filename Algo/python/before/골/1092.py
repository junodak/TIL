n = int(input())
n_arr = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
m_arr = sorted(list(map(int, input().split())), reverse=True)

if n_arr[0] < m_arr[0]:
    print(-1)
else:
    cnt = 0
    while m_arr:
        for i in n_arr:
            for j in range(len(m_arr)):
                if i >= m_arr[j]:
                    m_arr.pop(j)
                    break
        cnt += 1
    print(cnt)