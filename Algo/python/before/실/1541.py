# '-'다음에 '+'가 나오면 다음 '-'가 나오기 전까지 괄호로 묶기

# - 로 구분해서 리스트에 저장
text = input().split('-')

for i in range(len(text)):
    # 구분된 각 원소들을 '+'로 구분해서 int로 바꾸고 리스트로 바꾸고 합을 계산해서 다시 저장
    text[i] = sum(list(map(int, text[i].split('+'))))

# 처음값은 양수, 나머지는 음수로 계산해서 결과 계산
print(text[0] - sum(text[1:]))