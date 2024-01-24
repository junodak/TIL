def pow(x, y):
    print(x)
    print(y)

    return x
    
def rem(x, y):
    print(x)
    print(y)

    return x

a, b, c = map(int, input().split())
# 2진수로 변환
a_bin = bin(a)[2:]
b_bin = bin(b)[2:]
c_bin = bin(c)[2:]

# 제곱 계산
a_pow_b = pow(a_bin, b_bin)

# 나머지 계산
result_bin = rem(a_pow_b,c_bin)

# 나머지 10진법으로 출력 
print(int(result_bin,2))

