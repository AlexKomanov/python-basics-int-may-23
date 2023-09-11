words = ['java', 'python', 'javascript', 'php', 'typescript']

# words_with_position = list(enumerate(words, start=1))
#
# # Replace indices with values
# words_with_position = [(word, position) for position, word in words_with_position]
#
# print(words_with_position)

# Option 2

words_with_position = []
for index, value in enumerate(words, start=1):
    words_with_position.append((value, index))
print(words_with_position)
