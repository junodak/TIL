# 단어는 최대 10개, 단어 길이는 최대 8자리
# 1. len이 8이면 9, 7이면 9, 6이면 8
# 2. 

n = input()
word1 = input()
word2 = input()
i='9'
if len(word1)>len(word2):
    # 미리저장
    word1 = word1.replace(word1[0],'')
print(word1)

# word1 = word1.replace('a','2')

# num = 9
# txt_len = 8
# while txt_len:
#     for i in range(n):
#         if len(words[i])>=txt_len:
#             pass