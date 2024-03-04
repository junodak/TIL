import numpy as np

def fibonacci(n):
    matrix = np.array([[1, 1], [1, 0]])
    result = np.array([[1, 0], [0, 1]])  # 단위 행렬

    while n > 0:
        if n % 2 == 1:
            result = np.dot(result, matrix)
        matrix = np.dot(matrix, matrix)
        n //= 2

    return result[0][1]

n = int(input("몇 번째 피보나치 수를 계산하시겠습니까?: "))
print(fibonacci(n))

# n = int(input())
# arr = [0,1,1]

# for i in range(n-1):
#     arr[2] = (arr[0] + arr[1]) % 1000000
#     arr[0] = arr[1]
#     arr[1] = arr[2]

# if n:
#     print(arr[1])
# else:
#     print(0)