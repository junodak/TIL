# 단어는 최대 10개, 단어 길이는 최대 8자리
# 1. len이 8이면 9, 7이면 9, 6이면 8
# 2. 

n = int(input())
words = []
for i in range(n):
    words.append(input())


words[0].replace('a','2')

print(words)

# num = 9
# txt_len = 8
# while txt_len:
#     for i in range(n):
#         if len(words[i])>=txt_len:
#             pass
            
