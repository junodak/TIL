def fibonacci(n):
    # n이 0이거나 1일 때는 그대로 반환
    if n <= 1:
        return n
    
    # 이미 계산된 값이 있는지 확인하기 위한 배열
    fib_values = [0] * (n + 1)
    fib_values[1] = 1  # 초기값 설정
    
    # 피보나치 수열 계산
    for i in range(2, n + 1):
        fib_values[i] = fib_values[i - 1] + fib_values[i - 2]
    
    return fib_values[n]

# n번째 피보나치 수열 출력
n = int(input("n을 입력하세요: "))
print(f"{n}번째 피보나치 수열은 {fibonacci(n)%1000000007}입니다.")
