# 단어는 최대 10개, 단어 길이는 최대 8자리
# 1. len이 8이면 9, 7이면 9, 6이면 8
# 2. 

n = int(input())
words = []
words_copy = []
words_len = []

for i in range(n):
    word = input()
    words.append(word)
    words_copy.append(word)
    words_len.append(len(word))

change = []
num = 9
change_alphabet = words_copy[words_len.index(max(words_len))][0]
change.append([str(num), change_alphabet])
for i in range(n):
    words_copy[i] = words_copy[i].replace(change_alphabet, str(num))
num -=1
for i in range(n):
    if words_copy[i][0].isalpha() == False:
        words_copy[i].

print(change)
print(words_copy)

# word1 = word1.replace(word1[0],'')
# word1 = word1.replace('a','2')

# num = 9
# txt_len = 8
# while txt_len:
#     for i in range(n):
#         if len(words[i])>=txt_len:
#             pass


# 가장 긴걸 찾고, 그 알파벳을 가장 큰수로
# 길이가 같다면 개수가 많은거로 배정, 개수도 같으면 다음 거 개수로
# 맨 앞에 숫자가 보이면 안보일때까지 없애기