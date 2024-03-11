a, b = map(int, input().split())
sum = [0] * 54  # 10^16 = 2^54

for i in range(1, 54):
    sum[i] = 2**(i-1) + 2*sum[i-1]  # 누적합

def one_cnt(n):
    cnt = 0
    num = bin(n)[2:]  # 2진법 0b 빼고 슬라이싱
    l = len(num)

    for i in range(l):
        if num[i] == '1':
            mul = l-i-1  # n에 가장 가까운 승수
            cnt += sum[mul] + (n - 2**mul +1)
            n -= 2**mul
    return cnt
    
print(one_cnt(b) - one_cnt(a-1))