A, B, C = map(int, input().split())

def power_modulo(A, B, C):
    result = 1
    A = A % C  # 초기값 설정
    while B > 0:
        # B의 이진수 표현에서 마지막 비트가 1이면 A^(2^i)를 결과에 곱함
        if B % 2 == 1:
            result = (result * A) % C
        # A를 제곱하여 줄임
        A = (A * A) % C
        B //= 2  # B를 오른쪽으로 1 비트씩 이동시킴
    return result

result = power_modulo(A, B, C)
print(result)