n = int(input())
n_weight = list(map(int, input().split()))
n_weight.sort(reverse=True)
m = int(input())
m_weight = list(map(int, input().split()))
m_weight.sort(reverse=True)

print(n_weight)
print(m_weight)

n_count = [0]*n
for i in range(n):
    for j in range(m):
        if n_weight[i] >= m_weight[j]:
            n_count[i] += 1
print('count : ', n_count)

m_weight.pop(?)

# if max(n_weight) < max(m_weight):
#     print(-1)
# else:

# 자기가 들수있는 박스의 개수를 구하고
# 자기 다음으로 약한 크레인의 박스 개수를 뺀게 최대
